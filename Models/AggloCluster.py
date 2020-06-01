from sklearn.cluster import KMeans, AgglomerativeClustering
import pandas as pd 

# read csv
df = pd.read_csv("incidentes-viales-c5.csv")

# User can define year and month for the training model
syear = 2016
smonth = 2

# It is recommended to keep the sample at or below 10k rows or it can incurr in memory issues
trainDf = df[np.logical_and(df['mes']==smonth, df['año_cierre']==syear)].sample(10000).dropna()
pointsDf = trainDf[['']]

print('num accidents:', trainDf.shape[0])

# Clusterize data into clusters using hierarchical clustering
# User can define number of clusters to group data by 
clusters = 5

# train phase 
agc = AgglomerativeClustering(n_clusters=clusters, affinity='euclidean', linkage='ward')
# Fit and add cluster id to the each row in the training dataframe
trainDf['cluster'] = agc.fit_predict(trainDf[['latitud', 'longitud']])

# User can define how many points to plot to map, recommended small numbers
samplePoints = 100
pointsDf = trainDf[['cluster', 'latitud', 'longitud']].sample(samplePoints)

# get genesis point of each cluster (hierarchical clustering) and add to a new dataframe
listOfMeanCoor = []
for i in trainDf['cluster'].unique():
    listOfMeanCoor.append({'cluster': i,
                          'lat': trainDf[trainDf['cluster']==i]['latitud'].mean(),
                          'lon': trainDf[trainDf['cluster']==i]['longitud'].mean()})
   
dfMean = pd.DataFrame(listOfMeanCoor)
print(dfMean)


# trainDf : has the same rows as the original df, but with an additional classification col
# dfMean : has the mean lat, long point for each cluster 
# pointsDf : has a sample n points of the trainDf to graph to map



# For each cluster, plot the coordinates according to their color
# Recommended to plot 10k points in a graph (use trainDf)
# 100 points otherwise (use pointsDf)
fig, ax = plt.subplots()
for i, cluster in trainDf.groupby('cluster'):
    _ = ax.scatter(cluster['latitud'], cluster['longitud'], s=15, label=i)
ax.legend()
ax.set_xlabel('Latitude')
ax.set_ylabel('Longitude')
ax.set_title('Agglomerative Clustering')
fig.set_figheight(11)
fig.set_figwidth(11)
plt.show()