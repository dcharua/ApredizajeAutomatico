from flask import Flask, request, render_template, session, redirect, Response
from flask_cors import CORS
import json
import pandas as pd
import numpy as np

# Relative imports
from api.stats import Stats
from api.prediction import Prediction

app = Flask(__name__)

CORS(app)

df = pd.read_csv("data/incidentes-viales-c5.csv")
# data_df1 = data["fecha_creacion"]
# data_df2 = data["incidente_c4"]
# df = pd.DataFrame({"fecha": data_df1, "incidente": data_df2})


def process_ingest(dataset_json_list):
    global df
    df = pd.d.DataFrame(dataset_json_list)


@app.route("/", methods=["GET"])
def data_table():
    global df

    return render_template(
        "index.html", tables=[df[:10].to_html(classes="data")]
    )


@app.route("/getjson", methods=("POST", "GET"))
def data_json():
    global df
    return df[:100].to_json(orient="records")


@app.route("/ingest", methods=["POST"])
def set_ingest():
    # Basic json format validation.
    if not request.json:
        return "Invalid Input Error", 422

    # Process incoming json ingest.
    try:
        process_ingest(request.json)
        # Returns successful no content success.
        return "", 204
    except:
        # Unhandled errors should be taken care of.
        return "Internal Server Error", 500


@app.route("/predict", methods=["GET"])
def handle_prediction():
    global df

    try:
        # Parse query params.
        model = request.args.get("model", default=None, type=str)
        column = request.args.get("column", default=None, type=str)
        value = request.args.get("value", default=None, type=str)

        # Instantiate prediction class.
        predictions = Prediction(df)

        # If all query params are found call the queried model with params.
        if model and column and value:
            output = predictions.predict(model, column, value)
            print(output)
            return output

        # Return 422 if model, column, and value were not provided.
        return "Invalid Input Error", 422
    except AttributeError:
        # Handle if Prediction class did not find requested model.
        return "Model Not Found Error", 403
    except:
        # Unhandled errors should be taken care of.
        return "Internal Server Error", 500


# Get Statistical Estimations given a query param.
@app.route("/basic-stats", methods=["GET"])
def get_stats():
    global df

    # Parse query params.
    column = request.args.get("column", default=None, type=str)

    # Baisc input validation.
    if column is None or column not in df.columns:
        return "Invalid Input Error", 422

    # Return basic stats by queried column.
    try:
        currenct_df_stats = Stats(df)
        return currenct_df_stats.get_stats(column)
    except:
        # Unhandled errors should be taken care of.
        return "Internal Server Error", 500
