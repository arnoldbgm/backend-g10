from app import app
from controllers.usuarios_controller import UsuariosController
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity

@app.route("/auth/registrar", methods=['POST'])
def usuariosRegistrar():
    controller = UsuariosController()
    return controller.crearUsuario(request.json)

@app.route("/auth/autenticar", methods=['POST'])
def usuariosAutenticar():
    controller = UsuariosController()
    return controller.iniciarSesion(request.json)

@app.route("/auth/refresh", methods=['GET'])
@jwt_required(refresh = True)
def usuariosRefresh():
    identity = get_jwt_identity()
    controller = UsuariosController()
    return controller.refreshSesion(identity)