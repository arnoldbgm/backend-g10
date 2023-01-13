from flask import Flask
from os import environ
from configuracion import conexion
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_restful import Api

# El . es / que se una es Js
from models.categorias_model import Categoria
from models.productos_model import Producto
from models.categorias_productos_model import CategoriaProducto

# Controllers
from controllers.categoria_controller import CategoriaController, CategoriasController
# Aca utilizaremos las variables de entorno
load_dotenv()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get('DATABASE_URL')

# Inicialimamos nuestra clase Api
api = Api(app)

# Inicializar la aplicaicon de SqlAlchemy con nuestra aplicacion de flask
conexion.init_app(app)

# Inicializamos la casle Migrate pasondole nuestra aplicacion  de Flask y nuestra conexion de SQLAlchemy
Migrate(app,conexion)


# Asi utilizariamos la creacion de las tablas sin utilizar migraciones
# Este controlador se ejecutara antes dle primer request de nuestri servidor
@app.before_first_request
def inicializadora():
    # Realizara la cracion de todos los modelos de nuestro proyecto como tablas en bd
    # conexion.create_all()
    pass

api.add_resource(CategoriasController, '/categorias')
api.add_resource(CategoriaController, '/categoria/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)