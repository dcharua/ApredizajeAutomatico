from sklearn.linear_model import LinearRegression


# Obtener promedio de numero de accidentes por mes
x = sorted(list(df["mes"].unique()))
month = df['mes']
y = []

for i in range(1, 13):
    total = sum(1 for j in month if i == j)
    # dividir entre el numero de años
    y.append(int(total/7))

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
