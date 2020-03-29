# imports
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv("incidentes-viales-c5.csv")

# obtener numero de accidentes por mes 
x = sorted(list(df["mes"].unique()))
month = df['mes']
y = []

for i in range(1, 13):
    y.append(sum(1 for j in month if i == j))

# armar modelo
meanX = np.mean(x)
meanY = np.mean(y)

totalValues = len(x)
numer = 0
denom = 0

for i in range(totalValues):
    numer += (x[i] - meanX) * (y[i] - meanY)
    denom += (x[i] - meanX) ** 2
    
b1 = numer / denom
b0 = meanY - (b1 * meanX)


maxX = np.max(x) + 1
minX = np.min(x) - 1

x_ = np.linspace(minX, maxX, 1000)
y_ = b0 + b1 * x_

# grafica de regresion
plt.plot(x_, y_, label='Regresion linear')
plt.scatter(x, y)
plt.legend()
plt.show()

# predecir numero de accidentes en Enero
val = y_[x_==13]
