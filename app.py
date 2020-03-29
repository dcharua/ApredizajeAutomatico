from flask import Flask, request, render_template, session, redirect, Response
import json
import pandas as pd
import numpy as np

# Relative imports
from api.stats import Stats

app = Flask(__name__)

df = pd.read_csv("data/incidentes-viales.csv")
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
        "index.html", tables=[df.to_html(classes="data")], titles=df.columns.values
    )


@app.route("/getjson", methods=("POST", "GET"))
def data_json():
    global df
    return df.to_json(orient="records")


@app.route("/ingest", methods=["POST"])
def set_ingest():
    if not request.json:
        return "Invalid Input Error", 422
    try:
        process_ingest(request.json)
        return "", 204
    except:
        return "Internal Server Error", 500


# Get Statistical Estimations given a query param.
@app.route("/basic-stats", methods=["GET"])
def get_stats():
    global df

    column = request.args.get("column", default="", type=str)
    if column == "" or column not in df.columns:
        return "Invalid Input Error", 422

    try:
        currenct_df_stats = Stats(df)
        return currenct_df_stats.get_stats(column)
    except:
        return "Internal Server Error", 500
