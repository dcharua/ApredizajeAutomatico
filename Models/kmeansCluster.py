from sklearn.cluster import KMeans, AgglomerativeClustering
import math 
import pandas as pd
import numpy as np
from statistics import median
from math import radians, sin, cos, acos, atan2

# User can define year and month for the training model
syear = 2016
smonth = 2
# It is recommended to keep the sample at or below 10k rows or it can incurr in memory issues
trainDf = df[np.logical_and(df['mes']==smonth, df['año_cierre']==syear)].sample(10000).dropna()
#trainDf = df[(df['mes']==smonth) & (df['año_cierre']==syear)]

# train phase 
kmeans = KMeans(5)
clusters = kmeans.fit_predict(trainDf[['latitud','longitud']])
trainDf['k cluster'] = kmeans.predict(trainDf[['latitud','longitud']])

# User can define how many points to plot to map, recommended small numbers
samplePoints = 100
pointsDf = trainDf[['cluster', 'latitud', 'longitud']].sample(samplePoints)

# get mean point of each cluster (k-nearest) and add to new dataframe
listOfMeanCoor = []
for i in trainDf['k cluster'].unique():
    listOfMeanCoor.append({'kcluster': i,
                          'lat': trainDf[trainDf['k cluster']==i]['latitud'].mean(),
                          'lon': trainDf[trainDf['k cluster']==i]['longitud'].mean()})
    
dfMean = pd.DataFrame(listOfMeanCoor)

def measure(lat1, lon1, lat2, lon2):  # calculate physical distance between two points (meters)
    R = 6378.137; # Radius of earth in KM
    dLat = lat2 * math.pi / 180 - lat1 * math.pi / 180
    dLon = lon2 * math.pi / 180 - lon1 * math.pi / 180
    a = sin(dLat/2) * sin(dLat/2) + cos(lat1 * math.pi / 180) * cos(lat2 * math.pi / 180) * sin(dLon/2) * sin(dLon/2)
    c = 2 * atan2(math.sqrt(a), math.sqrt(1-a))
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