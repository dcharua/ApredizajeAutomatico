from sklearn.metrics import r2_score
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

# Obtener numero de accidentes por mes
x = sorted(list(df["mes"].unique()))
month = df['mes']
y = []

for i in range(1, 13):
    y.append(sum(1 for j in month if i == j))

# obtener modelo predictorio
# Sumatoria XY
xy = [a*b for a,b in zip(x,y)]
sumXY = sum(xy)

# Sumatoria X2
x2 = [a*b for a,b in zip(x,x)]
sumX2 = sum(x2)

# Sumatoria X3
x3 = [a*b for a,b in zip(x2,x)]
sumX3 = sum(x3)

# Sumatoria X4
x4 = [a*b for a,b in zip(x3,x)]
sumX4 = sum(x4)

# Sumatoria X5
x5 = [a*b for a,b in zip(x4,x)]
sumX5 = sum(x5)

# Sumatoria X5
x6 = [a*b for a,b in zip(x5,x)]
sumX6 = sum(x6)

# Sumatoria X2Y
x2y = [a*b for a,b in zip(x2,y)]
sumX2Y = sum(x2y)

# Sumatoria X3Y
x3y = [a*b for a,b in zip(x3,y)]
sumX3Y = sum(x3y)

sumX = sum(x)
sumY = sum(y)

n = len(x)

# Convertir en matriz
coffMat = np.matrix([[n, sumX, sumX2, sumX3], [sumX, sumX2, sumX3, sumX4], [sumX2, sumX3, sumX4, sumX5], [sumX3, sumX4, sumX5, sumX6]])
RHS = np.array([sumY, sumXY, sumX2Y, sumX3Y])

# matriz inversa 
invCoffMat = np.linalg.inv(coffMat)

# producto punto
coff = np.array(np.dot(invCoffMat, RHS))
coff = np.squeeze(np.asarray(coff))
a0, a1, a2, a3 = coff

# modelo de prediccion
X_ = np.linspace(np.min(x), np.max(x), n)
Y_ = a0 + a1*X_ + a2*(X_**2) + a3*(X_**3)
print("valores predecidos: ", Y_)

# certeza de prediccion
print("indice de prediccion", r2_score(y, Y_))

# grafica 
plt.scatter(x, y)
plt.plot(X_, Y_)
plt.show()