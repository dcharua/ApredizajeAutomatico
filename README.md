# ApredizajeAutomatico

---

##### Integrantes:
1. *Daniel Charua Garcia* - *A01017419*
2. *Kyungtak Woo* - *A01372055*
3. *Eduardo Badillo* - *A01020716*
4. *Enrique Vadillo* - *A01018714*
5. *David Gonzalez* - *A01019873*
---

### 0 Docs
Ejemplo práctico de cómo funciona su API se encuentra en la siguiente liga:
https://docs.google.com/document/d/1hkYu3gl8QdzsJsMmM2OYcL-rFRi5klV-TZEwHLI6B78/edit?usp=sharing

### 1 Introducción
Es una realidad que en la Ciudad México se depende del transporte automovilistico de manera diaria. Existen más de 4.7 millones de vehículos automotores registrados en la ciudad, ya sean de uso privado o de uso público. Debido al alto aforo vehicular se registran un promedio diario de 1,095 accidentes viales de diferente caracter en la capital del país, posicionando a la ciudad en tercer lugar dentro de México. A nivel nacional el 2.2% de las defunsiones son a causa de accidentes de tránsito. 
Afortunadamente se han realizado recompilación de datos de dichos accidentes y utilizando técnicas estadísticas, técnicas de machine learning y el uso de datasets de accidentes automovilísticos en la ciudad de México obtendremos predicciones, patrones y tendencias para poder predecir accidentes futuros y sus particularidades. Al encontrar patrones específicos podremos identificar en qué zonas, fechas, horas u otras variables influyen en la ocurrencia de accidentes automovilísticos, y se pueden elaborar sugerencias y precauciones para curvar estas cifras. 

### 2 Datos
Para el dataset se descargo de la [pagina de datos abiertos de la CDMX](https://datos.cdmx.gob.mx/explore/dataset/incidentes-viales-c5/table/?disjunctive.incidente_c4&refine.ano=2020&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJsaW5lIiwiZnVuYyI6IkFWRyIsInlBeGlzIjoibGF0aXR1ZCIsInNjaWVudGlmaWNEaXNwbGF5Ijp0cnVlLCJjb2xvciI6IiM2NmMyYTUifV0sInhBeGlzIjoibWVzZGVjaWVycmUiLCJtYXhwb2ludHMiOiIiLCJ0aW1lc2NhbGUiOm51bGwsInNvcnQiOiIiLCJjb25maWciOnsiZGF0YXNldCI6ImluY2lkZW50ZXMtdmlhbGVzLWM1Iiwib3B0aW9ucyI6eyJkaXNqdW5jdGl2ZS5pbmNpZGVudGVfYzQiOnRydWV9fX1dLCJkaXNwbGF5TGVnZW5kIjp0cnVlLCJhbGlnbk1vbnRoIjp0cnVlLCJ0aW1lc2NhbGUiOiIifQ%3D%3D) los reportes de accidentes viales en los que va del 2020 en la Cíudad de México.

### 3 Aplicación web (API)
La API fue desarrollada con [Flask](https://flask.palletsprojects.com/en/1.1.x/), se decidio usar esta opción ya que permite usar Python como lenguaje de programación, con todas su librerias de datos y machine learning, y de manera muy sencilla mostarar la infromación en paginas web.

#### 3.1 Instalación
Para correr la aplicación se debe clonar este repo y, acceder a la carpeta, crear un ambiente virtual y instalar los requerimentos de flask con los siguientes comandos:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=app.py
```

Posteriormente se debe correr la aplicación con el comando
```
flask run
```

#### 3.2 Dependencias
Las siguientes dependencias fueron usadas para el programa
- Flask -> para generar la aplicación web
- pandas -> para cargar la base de datos
- numpy -> como auxliar para panda y manipulación de los datos
- falta todas las de el modelo y las predcciones

#### 3.3 Endpoints
| Endpoint 	| Método 	| Formato 	| Regreso 	| Errores 	|
|-------------	|----------	|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|--------------------------------------------------------------------------------------------------------	|
| / 	| GET 	| curl --request GET --url 'http://127.0.0.1:5000/ 	| Tabla con toda la base de datos 	| - 	|
| predict 	| GET 	| 1.- curl --request GET --url 'http://127.0.0.1:5000/predict?model=linear_LSR&amp;column=mes&amp;value=5&= 2.- curl --request GET --url 'http://127.0.0.1:5000/predict?model=sklearn_linear_LSR&amp;column=mes&amp;value=3&=  3.- curl --request GET --url 'http://127.0.0.1:5000/predict?model=polynomial_LSR&amp;column=mes&amp;value=10&= 	| 1.- {   "model": "linear_LSR",   "input": {     "model": "linear_LSR",     "column": "mes",     "value": "5"   },   "prediction": {     "y": 15249.308857808857   } }    2.- {   "model": "sklearn_linear_LSR",   "input": {     "model": "sklearn_linear_LSR",     "column": "mes",     "value": "3"   },   "prediction": {     "y": 14959.210955710956,     "r_sq": 0.1869050297875251   } }   3.- {   "model": "polynomial_LSR",   "input": {     "model": "polynomial_LSR",     "column": "mes",     "value": "10"   },   "prediction": {     "y": 16614.988011987298,     "r_sq": 0.6746019277743616   } } 	| 422 si no se proporciona modelo, columna o valor;  403 si no se encontró el modelo;  500 error interno 	|
| ingest 	| POST 	| curl --request POST \   --url http://127.0.0.1:5000/ingest \   --header 'content-type: application/json' \   --data '[     {         "folio": "C5/2001010/05202",         "fecha_creacion": "01/01/2020",         "hora_creacion": "12:17:31",         "dia_semana": "Miercoles",         "codigo_cierre": "La unidad de atención a emergencias fue despachada, llegó al lugar de los hechos y confirmó la emergencia reportada",         "año cierre": "2020",         "mes_cierre": "Enero",         "hora_cierre": "13:39:38",         "delegacion_inicio": "CUAUHTEMOC",         "incidente_c4": "accidete-choque con lesionados",         "latitud": "19.42534",         "longitud": "-99.15655",         "clas_con_f_alarma": "URGENCIAS MEDICAS",         "tipo_entrada": "LLAMADO DEL 911",         "delegacion_cierre": "CUAUHTEMOC",         "geopoint": "19.42533999",         "mes": "1"     } ] 	| - 	| 204 sin contenido; 500 error interno 	|
| basic-stats 	| GET 	| curl --request GET --url 'http://127.0.0.1:5000/basic-stats?column=latitud&= 	| { "latitud": "-99.655"} 	| 422 input inválido;  500 error interno 	|
| getjson 	| POST GET 	| curl --request GET --url 'http://127.0.0.1:5000/getjson curl --request POST --url 'http://127.0.0.1:5000/getjson 	| Regresa los datos de la base de datos en formato JSON 	| - 	|