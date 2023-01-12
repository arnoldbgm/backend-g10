from configuracion import conexion
from sqlalchemy import Column, types

class Categoria(conexion.Model):
    # Estamos indicando que esta clase se comportara ademas como si fuera una tabla en la base de datos
    # https://docs.sqlalchemy.org/en/14/core/metadata.html#sqlalchemy.schema.Column.__init__

    # id INT AUTOINCREMENT PK
    id = Column(type_= types.Integer, autoincrement = True, primary_key = True)

    # https://docs.sqlalchemy.org/en/14/core/type_basics.html#generic-camelcase-types

    # nombre VARCHAR(45) NOT NULL UNIQUE
    nombre = Column(type_ = types.String(length=45), nullable = False, unique = True)

    # Para indicar el nombre en la base de datos
    __tablename__ = 'categorias'