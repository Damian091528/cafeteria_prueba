from flask import Flask, render_template # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore
import os

app = Flask(__name__)

# Base de datos SQLite local
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'cafeteria.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de tabla Menú
class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)

# Crear la base de datos y tabla si no existen
with app.app_context():
    db.create_all()

    # Si no hay datos, los agregamos como prueba
    if Menu.query.count() == 0:
        ejemplo = [
            Menu(nombre='Café', precio=1.50),
            Menu(nombre='Empanada', precio=2.00),
            Menu(nombre='Jugo Natural', precio=1.25)
        ]
        db.session.add_all(ejemplo)
        db.session.commit()

@app.route('/')
def index():
    menu_items = Menu.query.all()
    return render_template('prueba_de_cafeteria_2.html', menu=menu_items)

if __name__ == '__main__':
    app.run(debug=True)
