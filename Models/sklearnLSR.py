from sklearn.linear_model import LinearRegression


# Obtener numero de accidentes por mes
x = sorted(list(df["mes"].unique()))
month = df['mes']
y = []

for i in range(1, 13):
    y.append(sum(1 for j in month if i == j))

# hacer x bidimensional
X = np.array(x).reshape((-1,1))
Y = np.array(y)

# generar modelo
model = LinearRegression().fit(X, Y)

# r2 certeza
r_sq = model.score(X,Y)
print('r2 : ', r_sq)

# generar prediccion
y_prediccion = model.predict(X)
print('valores predecidos : ', y_prediccion)