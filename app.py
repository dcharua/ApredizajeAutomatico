from flask import Flask, request, render_template, session, redirect
import json
import pandas as pd
import numpy as np

app = Flask(__name__)

data = pd.read_csv("data/incidentes-viales.csv")
data_df1 = data['fecha_creacion']
data_df2 = data['incidente_c4']
df = pd.DataFrame({'fecha':data_df1,
                'incidente':data_df2
                })
                
@app.route('/', methods=("POST", "GET"))
def data_table():
     return render_template('index.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)

@app.route('/getjson', methods=("POST", "GET"))
def data_json():
    return df.to_json(orient='records')
