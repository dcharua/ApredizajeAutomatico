# Moved from /Models by @kevinwkt.
import base64
import inspect
import io
import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.cluster import KMeans, AgglomerativeClustering

class Cluster():
    def __init__(self, df):
        self.df = df
    
    # Switch with dispatcher method.
    def cluster(self, model, month, year, clusters):
        print('????')
        return getattr(self, model)(month, year, clusters)
    
    def agglo_cluster(self, smonth = 2, syear = 2016, sclusters = 5):
        print('1')
        # It is recommended to keep the sample at or below 10k rows or it can incurr in memory issues
        trainDf = self.df[np.logical_and(self.df['mes'] == smonth, self.df['año_cierre'] == syear)].sample(10000).dropna()

        print('2')
        ## Clusterize data into clusters using hierarchical clustering
        # Training phase.
        agc = AgglomerativeClustering(n_clusters=sclusters, affinity='euclidean', linkage='ward')
        print('2.1')
        # Fit and add cluster id to the each row in the training dataframe.
        trainDf['cluster'] = agc.fit_predict(trainDf[['latitud', 'longitud']])

        print('3')
        # User can define how many points to plot to map, recommended small numbers.
        samplePoints = 100
        pointsDf = trainDf[['cluster', 'latitud', 'longitud']].sample(samplePoints)

        # Get genesis point of each cluster (hierarchical clustering) and add to a new dataframe.
        listOfMeanCoor = []
        for i in trainDf['cluster'].unique():
            listOfMeanCoor.append({'cluster': i,
                                  'lat': trainDf[trainDf['cluster']==i]['latitud'].mean(),
                                  'lon': trainDf[trainDf['cluster']==i]['longitud'].mean()})

        print('4')
        dfMean = pd.DataFrame(listOfMeanCoor)
        print('5')


        # trainDf : has the same rows as the original df, but with an additional classification col.
        # dfMean : has the mean lat, long point for each cluster.
        # pointsDf : has a sample n points of the trainDf to graph to map.



        ## Plot image to send back.
        # For each cluster, plot the coordinates according to their color.
        # Recommended to plot 10k points in a graph (use trainDf).
        # 100 points otherwise (use pointsDf).
        print('6')
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
        print('7')

        pic_IObytes.seek()
        pic_hash = base64.b64encode(pic_IObytes.read())

        input_dict = {
            "model": inspect.stack()[0][3],
            "year": syear,
            "month": smonth,
            "clusters": sclusters,
        }
        output_dict = {
            
        }
        print('8')
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