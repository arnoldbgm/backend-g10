from flask import Flask, request
from flask_mysqldb import MySQL
# Devuelve todas las variables de entonrno del entorno
from os import environ
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
# Cuando usamos el environ llamamos usando el metodo get, solo es para
# para obtener  un valor y si el valor no se encuentro se colocara none
# este metodo busca dentro de las vari de entorno y jalar el valor del key
app.config['MYSQL_HOST'] = environ.get('MYSQL_HOST')
app.config['MYSQL_USER'] = environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = environ.get('MYSQL_DB')
app.config['MYSQL_PORT'] = int(environ.get('MYSQL_PORT'))

# Cuando a una variable se le asigne una clase se le llama INSTANCIA
# Iniciamos la conexion seteamos todos los parametros
mysql = MySQL(app)

@app.route('/productos', methods=['GET','POST'])
def gestion_productos():
    if request.method == 'GET':
        # Esto crea una conexion ala bd mediante un cursos
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall() #Limit infinito
        # cursor.fetchone() devuelve un #Limit 1
        print(productos)
        # Cerrar la conexion
        cursor.close()
        resultado=[]
        for producto in productos:
            producto_dic = {
                'id': producto[0],
                'nombre': producto[1],
                'imagen': producto[2],
                'fecha_vencimiento': producto[3].strftime('%Y-%m-%d'), #%H:%M:%S
                'precio': producto[4],
                'disponible': producto[5],
                'categoria_id': producto[6]
            }
            resultado.append(producto_dic)
            print(producto_dic)
        return{
            'message': 'Los productos son',
            'content': resultado
        }
    elif request.method == 'POST':
        cursor = mysql.connection.cursor()
        informacion = request.get_json()
        # '%s' -> convierte el contenido a un string
        # %f -> convierte el contenido a un numero flotante
        # %d -> convierte el contenido a un numero entero
        cursor.execute("INSERT INTO productos (id,nombre,imagen,fecha_vencimiento,precio,disponible,categoria_id) VALUES(DEFAULT, '%s','%s','%s',%f, %s, %d)" % (
            informacion.get('nombre'),
            informacion.get('imagen'),
            informacion.get('fecha_vencimiento'),
            informacion.get('precio'),
            informacion.get('disponible'),
            informacion.get('categoria_id')
        ))
        # indicamos que el guardado sea permanente en la bd
        mysql.connection.commit()
        cursor.close()
        return{
            'message': 'Producto creado exitosamente'
        }

@app.route("/producto/<int:id>", methods = ['GET', 'PUT', 'DELETE'])
def gestion_un_producto(id):
    pass


# Load_dotenv > cargamos todas las variables dentro del archivo .env
app.run(debug=True)