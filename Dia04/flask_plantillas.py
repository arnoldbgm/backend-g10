from flask import Flask, render_template
from os import environ
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <p>HOLA DESDE EL BAC</p>
    <h1>GOO</h1>"""

@app.route("/productos")
def productos():
    # TAREA: CONSUMIR LA BASE DE DATOS PARA DEVOLVER LOS RESULTADOS
    lista_productos = [
        {
            'id': 1,
            'nombre': 'coliflor',
            'precio': 4.5
        },
        {
            'id': 2,
            'nombre': 'manzana',
            'precio': 2.5
        },
        {
            'id': 3,
            'nombre': 'pera',
            'precio': 2.5
        },
    ]
    return render_template("listar-productos.html",  nombre='Arnold', lista_productos=lista_productos )

app.run(debug=True)