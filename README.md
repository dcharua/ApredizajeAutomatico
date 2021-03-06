﻿# ApredizajeAutomatico
![Logo](assets/logo.PNG)

---
##### Integrantes:
1. *Daniel Charua Garcia* - *A01017419*
2. *Kyungtak Woo* - *A01372055*
3. *Eduardo Badillo* - *A01020716*
4. *Enrique Vadillo* - *A01018714*
5. *David Gonzalez* - *A01019873*
---


## Definición

### 1. Problemática
Es una realidad que en la Ciudad México se depende del transporte automovilístico de manera diaria. Existen más de 4.7 millones de vehículos automotores registrados en la ciudad, ya sean de uso privado o de uso público. Debido al alto aforo vehicular se registran un promedio diario de 1,095 accidentes viales de diferente carácter en la capital del país, posicionando a la ciudad en tercer lugar dentro de México. A nivel nacional el 2.2% de las defunciones son a causa de accidentes de tránsito. 
Afortunadamente se han realizado recopilación de datos de dichos accidentes y utilizando técnicas estadísticas, técnicas de machine learning y el uso de datasets de accidentes automovilísticos en la ciudad de México obtendremos predicciones, patrones y tendencias para poder predecir accidentes futuros y sus particularidades. Al encontrar patrones específicos podremos identificar en qué zonas, fechas, horas u otras variables influyen en la ocurrencia de accidentes automovilísticos, y se pueden elaborar sugerencias y precauciones para curvar estas cifras. 

### 2. Objetivos
Objetivos Generales -> Elaborar una aplicación web con servicios que utilicen nuestros análisis de los datasets y proveer herramientas predictivas de manera que un usuario pueda ver índices de accidentes dentro de la Ciudad de México en el pasado y predicciones a futuro.

Objetivos Particulares -> Utilizando técnicas estadísticas, técnicas de machine learning y el uso de datasets de accidentes automovilísticos en la Ciudad de México obtener predicciones, patrones y tendencias para presentar información estadística relevante y poder predecir accidentes futuros y sus particularidades. Al encontrar patrones específicos podremos identificar en qué zonas, fechas, horas u otras variables influyen en la ocurrencia de accidentes automovilísticos, y se pueden elaborar sugerencias y precauciones para curvar estas cifras e incluso mejorar la movilidad.

### 3. Alcance 
El proyecto está diseñado como una herramienta para que los usuarios se puedan informar sobre la historia de los accidentes automovilístico en CDMX al despegar datos relevantes como horario con mayor accidentes, día de la semana con mayor accidentes, influencia de días festivos, etc. También el usuario puede tomar las predicciones como puntos de partida para tomar decisiones respecto al transporte en la ciudad. 

## Diseño de la arquitectura

![Arquitectura de la solución](assets/architecture.png)

## Backend

### 0. Docs
-Ejemplo práctico de cómo funciona su API se encuentra en la siguiente liga:
https://docs.google.com/document/d/1hkYu3gl8QdzsJsMmM2OYcL-rFRi5klV-TZEwHLI6B78/edit?usp=sharing
-Liga de la presentación:
https://docs.google.com/presentation/d/1J8jjnebgfKSmf1FMJRiPgqum8abmhp_32X-DxMp_GLA/edit?usp=sharing

### 1. Datos
Para el dataset se descargó de la [página de datos abiertos de la CDMX](https://datos.cdmx.gob.mx/explore/dataset/incidentes-viales-c5/table/?disjunctive.incidente_c4&refine.ano=2020&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJsaW5lIiwiZnVuYyI6IkFWRyIsInlBeGlzIjoibGF0aXR1ZCIsInNjaWVudGlmaWNEaXNwbGF5Ijp0cnVlLCJjb2xvciI6IiM2NmMyYTUifV0sInhBeGlzIjoibWVzZGVjaWVycmUiLCJtYXhwb2ludHMiOiIiLCJ0aW1lc2NhbGUiOm51bGwsInNvcnQiOiIiLCJjb25maWciOnsiZGF0YXNldCI6ImluY2lkZW50ZXMtdmlhbGVzLWM1Iiwib3B0aW9ucyI6eyJkaXNqdW5jdGl2ZS5pbmNpZGVudGVfYzQiOnRydWV9fX1dLCJkaXNwbGF5TGVnZW5kIjp0cnVlLCJhbGlnbk1vbnRoIjp0cnVlLCJ0aW1lc2NhbGUiOiIifQ%3D%3D) los reportes de accidentes viales en los que va del 2020 en la Ciudad de México.

### 2. Aplicación web (API)
La API fue desarrollada con [Flask](https://flask.palletsprojects.com/en/1.1.x/), se decidió usar esta opción ya que permite usar Python como lenguaje de programación, con todas su librerías de datos y machine learning, y de manera muy sencilla mostar la información en páginas web.

#### 2.1 Instalación
Para correr la aplicación se debe clonar este repo y, acceder a la carpeta, crear un ambiente virtual y instalar los requerimientos de flask con los siguientes comandos:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=app.py
```
La base de datos se puede agregar al proyecto con git lfs pull, si se tiene instalado, de los contrario se deberá [descargar](https://datos.cdmx.gob.mx/explore/dataset/incidentes-viales-c5/download/?format=csv&timezone=America/Mexico_City&lang=es&use_labels_for_header=true&csv_separator=%2C) y agregar a la carpeta de data manualmente

Posteriormente se debe correr la aplicación con el comando
```
flask run
```

#### 2.2 Dependencias
Las siguientes dependencias fueron usadas para el programa:
- Flask -> para generar la aplicación web
- pandas -> para cargar la base de datos
- numpy -> como auxiliar para panda y manipulación de los datos
- jsnon -> utilizada para trabajar con datos JSON
- sklearn -> herramienta para procesamiento de datos
- matplotlib -> herramienta para visualización

#### 2.3 Endpoints
| Endpoint 	| Método 	| Formato 	| Regreso 	| Errores 	|
|-------------	|----------	|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|--------------------------------------------------------------------------------------------------------
| predict 	| GET 	| 1.- curl --request GET \ --url 'http://localhost:5000/predict?column=mes&model=linear_LSR&value=5' 2.- curl --request GET \--url 'http://localhost:5000/predict?column=mes&model=sklearn_linear_LSR&value=5'  3.- curl --request GET \ --url 'http://localhost:5000/predict?column=mes&model=polynomial_LSR&value=5' 	| 1.- {   "model": "linear_LSR",   "input": {     "model": "linear_LSR",     "column": "mes",     "value": "5"   },   "prediction": {     "y": 15249.308857808857   }, "plot":{ "iVBORw0KGgo...  }    2.- {   "model": "sklearn_linear_LSR",   "input": {     "model": "sklearn_linear_LSR",     "column": "mes",     "value": "3"   },   "prediction": {     "y": 14959.210955710956, 16252.6594203283241...    "r_sq": 0.8169050297875251   } , "plot":"iVBORw0KGgo...." }   3.- {   "model": "polynomial_LSR",   "input": {     "model": "polynomial_LSR",     "column": "mes",     "value": "5"   },   "prediction": {     "y": 16614.988011987298, 15228.995004995493, ...    "r_sq": 0.6746019277743616   }, "plot":"iVBORw0KGgo...."} 	| 422 si no se proporciona modelo, columna o valor;  403 si no se encontró el modelo;  500 error interno 	|
| ingest 	| POST 	| curl --request POST \ --url http://127.0.0.1:5000/ingest \   --header 'content-type: application/json' \   --data '[     {         "folio": "C5/2001010/05202",         "fecha_creacion": "01/01/2020",         "hora_creacion": "12:17:31",         "dia_semana": "Miercoles",         "codigo_cierre": "La unidad de atención a emergencias fue despachada, llegó al lugar de los hechos y confirmó la emergencia reportada",         "año cierre": "2020",         "mes_cierre": "Enero",         "hora_cierre": "13:39:38",         "delegacion_inicio": "CUAUHTEMOC",         "incidente_c4": "accidete-choque con lesionados",         "latitud": "19.42534",         "longitud": "-99.15655",         "clas_con_f_alarma": "URGENCIAS MEDICAS",         "tipo_entrada": "LLAMADO DEL 911",         "delegacion_cierre": "CUAUHTEMOC",         "geopoint": "19.42533999",         "mes": "1"     } ] 	| - 	| 204 sin contenido; 500 error interno 	|
| basic-stats 	| GET 	| curl --request GET --url 'http://127.0.0.1:5000/basic-stats?column=latitud&=' 	| { "latitud": "-99.655"} 	| 422 input inválido;  500 error interno 	|
| getjson 	| POST GET 	| curl --request GET --url 'http://127.0.0.1:5000/getjson' curl --request POST --url 'http://127.0.0.1:5000/getjson'	| Regresa los datos de la base de datos en formato JSON 	| - 	|


## Frontend

### 1. Aplicación web (Frontend)
El front fue desarrollado con [React](https://reactjs.org/), se decidio usar esta opción ya que permite generar one page applications de manera sencilla y eficiente, además de tener mucho soporte y colaboración en la comunidad de desarrolladores

### 2. Instalación
Para correr la aplicación se debe clonar este repo y, acceder a la carpeta front, instalar los node_modules y correr la aplicación con los siguientes comandos:

```
cd front
npm install
npm run start
```

la aplicación se va a abrir en un navegador en el puerto 3000, se debe de tener el backend corriendo en otra terminal para poder generar las predicciones.
![Screenshot3](assets/sc3.jpg)
![Screenshot1](assets/sc1.png)
![Screenshot2](assets/sc2.png)

