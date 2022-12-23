from flask import Flask, request
from flask_cors import CORS

# si el archivo es el archivo principal del proyecto su valor de la variable __name__ sera '__main__' caso contrario sera None (vacio)
app = Flask(__name__)

# Ahora configuramos nuestros CORS
# corregir todos los origin origins='*'
# corregir todos los methods = '*'
CORS(app=app, origins=['http://127.0.0.1:5500'], methods=['GET', 'POST'])

# patron de diseño de software (Singleton)

usuarios = [
    {
        'nombre': 'Arnold',
        'apellido': 'Gallegos'
    },
    {
        'nombre': 'Diego',
        'apellido': 'Gallegos'
    },
    {
        'nombre': 'Pablo',
        'apellido': 'Castillo'
    }
]

# un decorador se usa con el '@' y sirve para poder modificar cierto metodo de una clase sin la necesidad de modificar el funcionamiento natural (es una modificacion parcial) luego de utilizar el decorador se crea una funcion que sera la nueva funcionabilidad de ese metodo
@app.route('/')
def inicio():
    return 'Hola desde mi servidor de Flask'

@app.route('/mostrar-hora', methods=['GET','POST'])
def saludo():
    # Controller es la funcionalibiladad que se realizara dentro de un determinado endpoint
    print(request.method)
    if request.method == 'GET':
        return {
            'content': 'Me hiciste un GET'
        }
    elif request.method == 'POST':
        return{
            'content': 'Me hiciste un POST'
        }
    # Esta parte sera inaccesible por que los metohos son get y post
    # PEro si añado en los metodos put recien me reterona la hora
    return {
        'content': '22:50:15'
    }

@app.route('/usuarios', methods=['GET', 'POST'])
def gestionUsuario():
    if request.method == 'GET':
        return {
            'message': 'Los usuarios son',
            'content': usuarios
        }
    elif request.method == 'POST':
        # Agregar un nuevo usuario
        # request.data-> mostra la info en foramto bytes

        # usamos get_json() -> para que este en un diccionario
        print(request.get_json())
        data = request.get_json()
        usuarios.append(data)
        return{
            'message': 'Usaurio agregado exitosamente'
        }

# debug > cada vez que modifiquemos algun archivo del proyecto y guardamos, se reiniciara el servidor
app.run(debug=True)