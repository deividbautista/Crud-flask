
# Apartado donde se importan todas las librerias necesarias para el correcto funcionamiento del proyecto.
from flask import Flask, render_template, request, redirect, url_for
import os
import database as db

# Apartado para configuración de las rutas del proyecto.
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__, template_folder = template_dir)

# Rutas de la aplicación.
@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM users")
    myresult = cursor.fetchall()
    # Convertir los datos a diccionario.
    insertObject = []
    # Insertar columnas con los datos
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('index.html', data=insertObject)

# Función para guardar usuarios en la Base de datos.
@app.route('/user', methods=['POST'])
def addUser():
    # Se reciben los parametros enviados por el formulario, para realizar el registro.
    username = request.form['NDI']
    name = request.form['fullname']
    password = request.form['password']

    # Se define la condicional que permitira realizar la consulta para insertar nuevos registros.
    if username and name and password:
        cursor = db.database.cursor()

        # Sentencia sql para insertar datos.
        sql = "INSERT INTO users (NDI, fullname, password) VALUES (%s, %s, %s)"

        # Se almacenan los datos en una tupla, para poder insertarlo de manera dinamica en la consulta.
        data = (username, name, password)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

# Función para borrar registros.
@app.route('/delete/<string:id>')
def delete(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM users WHERE id=%s"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('home'))

# Función para editar registros en la base de datos.
@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
    # Se reciben los parametros enviados por el formulario, para realizar la actualización.
    username = request.form['NDI']
    name = request.form['fullname']
    password = request.form['password']

    if username and name and password:
        cursor = db.database.cursor()
        sql = "UPDATE users SET NDI = %s, fullname = %s, password = %s WHERE id = %s"
        data = (username, name, password, id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

# Se da inicio al servidor, en el puerto "8000", con la propiedad "debug=True" que nos permite 
# realizar cambios en la app sin necesidad de desconectar el servidor, mientras estos cambios no 
# sean un problema que ocaciones bugs, o errores de sintaxis
if __name__ == '__main__':   
    app.run(debug=True, port=8000)