import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


# Obtener numero de accidentes por mes
x = sorted(list(df["mes"].unique()))
month = df['mes']
y = []

for i in range(1, 13):
    y.append(sum(1 for j in month if i == j))

# graficar accidentes x mes
plt.plot(x,y, label='accidentes por mes')
plt.legend()
plt.show()

# obtener modelo predictorio
# Sumatoria XY
xy = [a*b for a,b in zip(x,y)]
sumXY = sum(xy)

# Sumatoria X2
xx = [a*b for a,b in zip(x,x)]
sumXX = sum(xx)

sumX = sum(x)
sumY = sum(y)

n = len(x)

# pendiente 
a1 = (n*sumXY)-(sumX*sumY)
a1 = a1/((n*sumXX)-(sumX**2))

# c 
a0 = np.mean(y) - a1*np.mean(x)

# modelo de prediccion
ind = np.linspace(np.min(x), np.max(x), 12)
dep = a0 + a1 * ind
print('valores predecidos: ', dep)

# graficar modelo con regresion lineal
plt.plot(ind, dep, label='Regresion')
plt.scatter(x, y)
plt.legend()
plt.show()