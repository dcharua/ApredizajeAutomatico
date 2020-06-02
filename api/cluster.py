# Moved from /Models by @kevinwkt.
import base64
import inspect
import io
import json
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from math import radians, sin, cos, acos, atan2, pi, sqrt
from sklearn.cluster import KMeans, AgglomerativeClustering
from statistics import median

class Cluster():
    def __init__(self, df):
        self.df = df
    
    # Switch with dispatcher method.
    def cluster(self, model, month, year, clusters):
        return getattr(self, model)(month, year, clusters)
    
    def agglo_cluster(self, smonth = 2, syear = 2016, sclusters = 5):
        # It is recommended to keep the sample at or below 10k rows or it can incurr in memory issues
        trainDf = self.df[np.logical_and(self.df['mes']==smonth, self.df['año_cierre']==syear)].sample(10000).dropna()

        ## Clusterize data into clusters using hierarchical clustering
        # Training phase.
        agc = AgglomerativeClustering(n_clusters=sclusters, affinity='euclidean', linkage='ward')
        # Fit and add cluster id to the each row in the training dataframe.
        trainDf['cluster'] = agc.fit_predict(trainDf[['latitud', 'longitud']])

        # User can define how many points to plot to map, recommended small numbers.
        samplePoints = 100
        pointsDf = trainDf[['cluster', 'latitud', 'longitud']].sample(samplePoints)

        # Get genesis point of each cluster (hierarchical clustering) and add to a new dataframe.
        listOfMeanCoor = []
        for i in trainDf['cluster'].unique():
            listOfMeanCoor.append({'cluster': i,
                                  'lat': trainDf[trainDf['cluster']==i]['latitud'].mean(),
                                  'lon': trainDf[trainDf['cluster']==i]['longitud'].mean()})

        dfMean = pd.DataFrame(listOfMeanCoor)


        # trainDf : has the same rows as the original df, but with an additional classification col.
        # dfMean : has the mean lat, long point for each cluster.
        # pointsDf : has a sample n points of the trainDf to graph to map.



        ## Plot image to send back.
        # For each cluster, plot the coordinates according to their color.
        # Recommended to plot 10k points in a graph (use trainDf).
        # 100 points otherwise (use pointsDf).
        pic_IObytes = io.BytesIO()
        fig, ax = plt.subplots()
        for i, cluster in trainDf.groupby('cluster'):
            _ = ax.scatter(cluster['latitud'], cluster['longitud'], s=15, label=i)
        ax.legend()
        ax.set_xlabel('Latitude')
        ax.set_ylabel('Longitude')
        ax.set_title('Agglomerative Clustering')
        fig.set_figheight(11)
        fig.set_figwidth(11)
        plt.savefig(pic_IObytes, format='png')

        pic_IObytes.seek(0)
        pic_hash = base64.b64encode(pic_IObytes.read())

        input_dict = {
            "model": inspect.stack()[0][3],
            "year": syear,
            "month": smonth,
            "clusters": sclusters,
        }
        output_dict = {
            "dfPoints": pointsDf.to_json(),
        }
        response = self.create_response_payload(input_dict, output_dict, pic_hash)

        # Convert into response json.
        return json.dumps(response)

    def kmeans_cluster(self, smonth = 2, syear = 2016, sclusters = 5):
        # It is recommended to keep the sample at or below 10k rows or it can incurr in memory issues
        trainDf = self.df[np.logical_and(self.df['mes']==smonth, self.df['año_cierre']==syear)].sample(10000).dropna()
        #trainDf = df[(df['mes']==smonth) & (df['año_cierre']==syear)]

        # train phase 
        kmeans = KMeans(sclusters)
        clusters = kmeans.fit_predict(trainDf[['latitud','longitud']])
        trainDf['k cluster'] = kmeans.predict(trainDf[['latitud','longitud']])

        # User can define how many points to plot to map, recommended small numbers
        samplePoints = 100
        pointsDf = trainDf[['k cluster', 'latitud', 'longitud']].sample(samplePoints)

        # get mean point of each cluster (k-nearest) and add to new dataframe
        listOfMeanCoor = []
        for i in trainDf['k cluster'].unique():
            listOfMeanCoor.append({'k cluster': i,
                                  'lat': trainDf[trainDf['k cluster']==i]['latitud'].mean(),
                                  'lon': trainDf[trainDf['k cluster']==i]['longitud'].mean()})

        dfMean = pd.DataFrame(listOfMeanCoor)

        def measure(lat1, lon1, lat2, lon2):  # calculate physical distance between two points (meters)
            R = 6378.137; # Radius of earth in KM
            dLat = lat2 * pi / 180 - lat1 * pi / 180
            dLon = lon2 * pi / 180 - lon1 * pi / 180
            a = sin(dLat/2) * sin(dLat/2) + cos(lat1 * pi / 180) * cos(lat2 * pi / 180) * sin(dLon/2) * sin(dLon/2)
            c = 2 * atan2(sqrt(a), sqrt(1-a))
            d = R * c
            return d * 1000 # meters

        # Get distance from source to min, mean and max points
        # Any of these can be used for the cluster graphical radius 
        for i in dfMean['k cluster']:
            radiList = []

            # Get mean point for the cluster
            a = dfMean[dfMean['k cluster']==i]['lat'].values
            b = dfMean[dfMean['k cluster']==i]['lon'].values

            # filter data to that cluster in auxDf
            auxDf = trainDf[trainDf['k cluster']==i]

            # retrieve all distances from all points
            for x, y in zip(auxDf['latitud'], auxDf['longitud']):
                radiList.append(measure(a,b,x,y))

            # add max, mean and min points to dfMean
            dfMean.loc[dfMean['k cluster']==i, 'maxDistance'] = np.array(radiList).max()
            dfMean.loc[dfMean['k cluster']==i, 'meanDistance'] = np.array(radiList).mean()
            dfMean.loc[dfMean['k cluster']==i, 'minDistance'] = np.array(radiList).min()
            dfMean.loc[dfMean['k cluster']==i, 'medianDistance'] = median(radiList)
            

        pic_IObytes = io.BytesIO()
        fig, ax = plt.subplots()
        for i, cluster in trainDf.groupby('k cluster'):
            _ = ax.scatter(cluster['latitud'], cluster['longitud'], s=15, label=i)
        ax.legend()
        ax.set_xlabel('Latitude')
        ax.set_ylabel('Longitude')
        ax.set_title('K Means Clustering')
        fig.set_figheight(11)
        fig.set_figwidth(11)
        plt.savefig(pic_IObytes, format='png')

        pic_IObytes.seek(0)
        pic_hash = base64.b64encode(pic_IObytes.read())
        
        input_dict = {
            "model": inspect.stack()[0][3],
            "year": syear,
            "month": smonth,
            "clusters": sclusters,
        }
        output_dict = {
            "dfPoints": pointsDf.to_json(),
        }
        response = self.create_response_payload(input_dict, output_dict, pic_hash)

        # Convert into response json.
        return json.dumps(response)

    def create_response_payload(self, input_dict, output, plot = ""):
        cluster_json = {}
        cluster_json["model"] = input_dict["model"]
        cluster_json["input"] = input_dict
        cluster_json["cluster"] = output
        cluster_json["plot"] = plot.decode('utf-8')
        return cluster_json