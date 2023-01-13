from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.categorias_model import Categoria

class CategoriaDto(SQLAlchemyAutoSchema):
    class Meta:
        # Sirve para pasar los metadatos a la clase que estamos heredando
        # Metadatos son informacion que necesita la clase que estamos heredando como atributo para que funcione correctamente
        # Sirve para indicar mediante que modelo se tiene que guiar para eacer el modelo
        model = Categoria