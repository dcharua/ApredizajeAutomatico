from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures


# Expected value of monthly accidents
x = sorted(list(df["mes"].unique()))
month = df['mes']
y = []


for i in range(1, 13):
    total = sum(1 for j in month if i == j)
    # divide by number of years in dataset
    y.append(int(total/7))
    

# User Input Polynomial degree, reshape and fit data
polyDegree = 6

polynomial_features = PolynomialFeatures(degree=polyDegree)
x_poly = polynomial_features.fit_transform(np.array(x).reshape(-1, 1))

# Train model
model = LinearRegression()
model.fit(x_poly, y)
y_poly_pred = model.predict(x_poly)

print('predicted values', y_poly_pred)

# r2 score
r2 = r2_score(y,y_poly_pred)
print(r2)

# simple plot
plt.scatter(x, y, s=10)
plt.plot(x, y_poly_pred)
plt.show()
