from flask import Flask

# Con poner __name__ indicamos que se llamar a Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "mi aplicacion con Flask :D"

