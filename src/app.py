from flask import Flask, render_template
import os
import database as db
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__,template_folder = template_dir)

#Rutas
@app.route('/')
def home():
    Cursor = db.database.cursor()
    Cursor.execute("SELECT * FROM users")
    myresult = Cursor.fetchall()
    #
    InsertObject = []
    columnNames = [column[0] for column in Cursor.description]
    for record in myresult:
        InsertObject.append(dict(zip(columnNames, record)))
    Cursor.close()
    return render_template('index.html', data=InsertObject)

if __name__ == '__main__':
    app.run(debug=True)
