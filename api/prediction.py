# Moved from /Models by @kevinwkt.
import inspect
import json
import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score


class Prediction:
    def __init__(self, df):
        self.df = df

    # Switch with dispatcher method.
    def predict(self, model, column, value):
        return getattr(self, model)(column, value)

    # Linear LSR with ScikitLearn.
    def sklearn_linear_LSR(self, column, value):

        # HARDCODED Get average of numbers of accidents per month.
        x = sorted(list(self.df[column].unique()))
        month = self.df[column]
        y = []

        # HARDCODED to accept months for now.
        for i in range(1, 13):
            total = sum(1 for j in month if i == j)
            # Divide between number of years.
            y.append(int(total / 7))

        # Make x bidimensional.
        X = np.array(x).reshape((-1, 1))
        Y = np.array(y)

        # Generate model.
        model = LinearRegression().fit(X, Y)

        # Get r2 confidence.
        r_sq = model.score(X, Y)

        # Get prediction.
        y_prediction = model.predict(X)

        # Create response payload.
        input_dict = {
            "model": inspect.stack()[0][3],
            "column": column,
            "value": value,
        }
        output_dict = {
            "y": y_prediction[int(value)],
            "r_sq": r_sq,
        }
        response = self.create_response_payload(input_dict, output_dict)

        # Convert into response json.
        return json.dumps(response)

    def sklearn_polinomial_PLSR(self, column, value):
        x = sorted(list(df[column].unique()))
        month = df[column]
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
        
        # Create response payload.
        input_dict = {
            "model": inspect.stack()[0][3],
            "column": column,
            "value": value,
        }
        output_dict = {
            "y": y_poly_pred,
            "r_sq": r2_score(y, y_poly_pred),
        }
        response = self.create_response_payload(input_dict, output_dict)

        # Convert into response json.
        return json.dumps(response)        

    # Polynomial LSR without ScikitLearn.
    def polynomial_LSR(self, column, value):
        # HARDCODED Get average number of accidents per month.
        x = sorted(list(self.df[column].unique()))
        month = self.df[column]
        y = []

        # HARDCODED to accept months for now.
        for i in range(1, 13):
            total = sum(1 for j in month if i == j)
            # Divide between nuber of years.
            y.append(int(total / 7))

        # Sum XY.
        xy = [a * b for a, b in zip(x, y)]
        sumXY = sum(xy)

        # Sum X2.
        x2 = [a * b for a, b in zip(x, x)]
        sumX2 = sum(x2)

        # Sum X3.
        x3 = [a * b for a, b in zip(x2, x)]
        sumX3 = sum(x3)

        # Sum X4.
        x4 = [a * b for a, b in zip(x3, x)]
        sumX4 = sum(x4)

        # Sum X5.
        x5 = [a * b for a, b in zip(x4, x)]
        sumX5 = sum(x5)

        # Sum X5.
        x6 = [a * b for a, b in zip(x5, x)]
        sumX6 = sum(x6)

        # Sum X2Y.
        x2y = [a * b for a, b in zip(x2, y)]
        sumX2Y = sum(x2y)

        # Sum X3Y.
        x3y = [a * b for a, b in zip(x3, y)]
        sumX3Y = sum(x3y)

        sumX = sum(x)
        sumY = sum(y)

        n = len(x)

        # Convert to matrix.
        coffMat = np.matrix(
            [
                [n, sumX, sumX2, sumX3],
                [sumX, sumX2, sumX3, sumX4],
                [sumX2, sumX3, sumX4, sumX5],
                [sumX3, sumX4, sumX5, sumX6],
            ]
        )
        RHS = np.array([sumY, sumXY, sumX2Y, sumX3Y])

        # Get inverse matrix.
        invCoffMat = np.linalg.inv(coffMat)

        # Get dot product.
        coff = np.array(np.dot(invCoffMat, RHS))
        coff = np.squeeze(np.asarray(coff))
        a0, a1, a2, a3 = coff

        # Get prediction model.
        X_ = np.linspace(np.min(x), np.max(x), n)
        Y_ = a0 + a1 * X_ + a2 * (X_ ** 2) + a3 * (X_ ** 3)

        # Create response payload.
        input_dict = {
            "model": inspect.stack()[0][3],
            "column": column,
            "value": value,
        }
        output_dict = {
            "y": Y_[int(value)],
            "r_sq": r2_score(y, Y_),
        }
        response = self.create_response_payload(input_dict, output_dict)

        # Convert into response json.
        return json.dumps(response)

    # Linear LSR without ScikitLearn.
    def linear_LSR(self, column, value):
        # HARDCODED Get average number of accidents per month.
        x = sorted(list(self.df[column].unique()))
        month = self.df[column]
        y = []

        # HARDCODED to accept months for now.
        for i in range(1, 13):
            total = sum(1 for j in month if i == j)
            # Divide between nuber of years.
            y.append(int(total / 7))

        # Sum XY.
        xy = [a * b for a, b in zip(x, y)]
        sumXY = sum(xy)

        # Sum X2.
        xx = [a * b for a, b in zip(x, x)]
        sumXX = sum(xx)

        sumX = sum(x)
        sumY = sum(y)

        n = len(x)

        # Get gradiant.
        a1 = (n * sumXY) - (sumX * sumY)
        a1 = a1 / ((n * sumXX) - (sumX ** 2))

        # Get 'c'.
        a0 = np.mean(y) - a1 * np.mean(x)

        # Get predictive model.
        ind = np.linspace(np.min(x), np.max(x), 12)
        dep = a0 + a1 * ind

        # Create response payload.
        input_dict = {
            "model": inspect.stack()[0][3],
            "column": column,
            "value": value,
        }
        output_dict = {
            "y": dep[int(value)],
        }
        response = self.create_response_payload(input_dict, output_dict)

        # Convert into response json.
        return json.dumps(response)

    def create_response_payload(self, input_dict, output):
        prediction_json = {}
        prediction_json["model"] = input_dict["model"]
        prediction_json["input"] = input_dict
        prediction_json["prediction"] = output
        return prediction_json
