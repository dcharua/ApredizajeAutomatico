import math 
from statistics import median
from math import radians, sin, cos, acos, atan2

def calculateDistance(x1,y1,x2,y2):  # calculate hard distance between two cartesian points
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     return dist

def radianDistance(x1, y1, x2, y2):  # calculate radian distance between two points
    slat = radians(x1)
    slon = radians(y1)
    elat = radians(x2)
    elon = radians(y2)
    dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
    return dist

def measure(lat1, lon1, lat2, lon2):  # calculate physical distance between two points (meters)
    R = 6378.137; # Radius of earth in KM
    dLat = lat2 * math.pi / 180 - lat1 * math.pi / 180
    dLon = lon2 * math.pi / 180 - lon1 * math.pi / 180
    a = sin(dLat/2) * sin(dLat/2) + cos(lat1 * math.pi / 180) * cos(lat2 * math.pi / 180) * sin(dLon/2) * sin(dLon/2)
    c = 2 * atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    return d * 1000 # meters

# Get distance from source to min, mean and max points
for i in dfMean['cluster']:
    radiList = []
    
    # Get mean point for the cluster
    a = dfMean[dfMean['cluster']==i]['lat'].values
    b = dfMean[dfMean['cluster']==i]['lon'].values
    
    # filter data to that cluster in auxDf
    auxDf = trainDf[trainDf['cluster']==i]
    
    # retrieve all distances from all points
    for x, y in zip(auxDf['latitud'], auxDf['longitud']):
        radiList.append(measure(a,b,x,y))
        
    # add max, mean and min points to dfMean
    dfMean.loc[dfMean['cluster']==i, 'maxDistance'] = np.array(radiList).max()
    dfMean.loc[dfMean['cluster']==i, 'meanDistance'] = np.array(radiList).mean()
    dfMean.loc[dfMean['cluster']==i, 'minDistance'] = np.array(radiList).min()
    dfMean.loc[dfMean['cluster']==i, 'medianDistance'] = median(radiList)
dfMean