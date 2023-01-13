from flask_restful import Resource, request
from configuracion import conexion
from models.categorias_model import Categoria
from dtos.categoria_dto import CategoriaDto
from sqlalchemy.exc import IntegrityError
from marshmallow.exceptions import ValidationError


# Ahora en esta clase podre utilizar los metodos HTTP
class CategoriasController(Resource):
    def get(self):
        # all => select * from categorias
        data = conexion.session.query(Categoria).all()
        print(data[0])
        # many = True > indica que le vamos a pasar una lista de instancias y el DTO la tendra que iterrar par poder convertir
        serializador = CategoriaDto(many=True)
        # dump> convierte la instancia de la clase en un diccionario
        resultado = serializador.dump(data)
        return{
         'content': resultado
        }
    def post(self):
        data = request.get_json()
        print(data)
        serializador = CategoriaDto()
        # load -> valida el diccionario que cumpla con todas las carecteristicas de las columnas de nuestro modelo y si es devolvera un diccionario con la informacion necesaria
        try:
            resultado = serializador.load(data)
            print(resultado)
            # Inicializamos nuestra nueva pero aun no la guardamos
            nuevaCategoria = Categoria(nombre = resultado.get('nombre'))
            # Agregamos un new element
            conexion.session.add(nuevaCategoria)
            # Ahora gurdamos
            conexion.session.commit()
            return{
                'message': 'Categoria gurada exitosamente'
            }

        except IntegrityError as error_integridad:
            return{
                'message': 'Error esa categoria ya existe ^-^'
            }

        except ValidationError as error_validacion:
            return{
                'message': 'Error al crear la categoria, vea el content',
                'content': error_validacion.args
            }

        except Exception as error:
            return{
                'message': 'Error al crear la categoria',
                'content': error.args
            }

class CategoriaController(Resource):
    def get(self,id):
        print(id)
        # SELECT * FROM categorias WHERE id = ... LIMIT = 1;
        # first < no devuelve una lista sino devuelve una instancia o None
        # all > me devolvera una lisa con todas las coincidencidas
        categoria = conexion.session.query(Categoria).filter_by(id = id).first()
        print(categoria)
        # TODO: Convertir esta cat para mostrar en el contet, si es que la categoria no existe (NONE) indicar que la categoria no existe en el 'message
        return{
            'content': ''
        }

        # <Categoria1> es una sola instancia es como un elemento del array
        # [<Categoria1> ] es un arreglo