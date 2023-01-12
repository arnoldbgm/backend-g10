from flask import Flask
from os import environ
from configuracion import conexion
from dotenv import load_dotenv
# El . es / que se una es Js
from models.categorias_model import Categoria

# Aca utilizaremos las variables de entorno
load_dotenv()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get('DATABASE_URL')

# Inicializar la aplicaicon de SqlAlchemy con nuestra aplicacion de flask
conexion.init_app(app)

# Este controlador se ejecutara antes dle primer request de nuestri servidor
@app.before_first_request
def inicializadora():
    # Realizara la cracion de todos los modelos de nuestro proyecto como tablas en bd
    conexion.create_all()

if __name__ == '__main__':
    app.run(debug=True)