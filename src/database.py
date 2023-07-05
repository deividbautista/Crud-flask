#-----------------------------------------------------
#Apartado en el que se configura los datos del usuario.
#-----------------------------------------------------

import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='crud-flask_2'
)
