# ApredizajeAutomatico

---

##### Integrantes:
1. *Daniel Charua Garcia* - *A01017419*
2. *Kyungtak Woo* - *A01372055*
3. *Eduardo Badillo* - *A01020716*
4.
5.
---

### 0 Docs
Documentación donde explique los formatos para la ingesta de datos, tutorial de como correr el proyecto, así como un ejemplo práctico de cómo funciona su API se encuentra en la siguiente liga:
https://docs.google.com/document/d/1hkYu3gl8QdzsJsMmM2OYcL-rFRi5klV-TZEwHLI6B78/edit?usp=sharing

### 1 Introducción
En la Ciudad México existen 4.7 millones de vehículos automotores registrado, gran parte de la población depende de este medio de transporte. Debido al alto aforo vehicular se registran un promedio diario de 1,095 accidentes viales en la capital del país


### 2 Datos
Para el dataset se descargo de la [pagina de datos abiertos de la CDMX](https://datos.cdmx.gob.mx/explore/dataset/incidentes-viales-c5/table/?disjunctive.incidente_c4&refine.ano=2020&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJsaW5lIiwiZnVuYyI6IkFWRyIsInlBeGlzIjoibGF0aXR1ZCIsInNjaWVudGlmaWNEaXNwbGF5Ijp0cnVlLCJjb2xvciI6IiM2NmMyYTUifV0sInhBeGlzIjoibWVzZGVjaWVycmUiLCJtYXhwb2ludHMiOiIiLCJ0aW1lc2NhbGUiOm51bGwsInNvcnQiOiIiLCJjb25maWciOnsiZGF0YXNldCI6ImluY2lkZW50ZXMtdmlhbGVzLWM1Iiwib3B0aW9ucyI6eyJkaXNqdW5jdGl2ZS5pbmNpZGVudGVfYzQiOnRydWV9fX1dLCJkaXNwbGF5TGVnZW5kIjp0cnVlLCJhbGlnbk1vbnRoIjp0cnVlLCJ0aW1lc2NhbGUiOiIifQ%3D%3D) los reportes de accidentes viales en los que va del 2020 en la Cíudad de México

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

#### 3.3 Enpoints
- / -> En el home se muestra una tabla con la infromación cargada de la base de datos en local
- /getjson -> Regresa los datos en forma de JSON
