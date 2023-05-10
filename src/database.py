#Importamos la libreria de mysql, que utilizaremos para poder
#realizar consultas SQL
import mysql.connector

#Tenemos la configuración sobre la base de datos para poder
#realizar la conección.
database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='crud-flask'
)