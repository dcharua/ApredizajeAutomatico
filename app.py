from flask import Flask, request, render_template, session, redirect, Response
import json
import pandas as pd
import numpy as np

app = Flask(__name__)

data = pd.read_csv("data/incidentes-viales.csv")
data_df1 = data["fecha_creacion"]
data_df2 = data["incidente_c4"]
df = pd.DataFrame({"fecha": data_df1, "incidente": data_df2})


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
