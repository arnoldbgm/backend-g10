from models.usuarios_model import UsuariosModel
from werkzeug.security import generate_password_hash, check_password_hash
from db import db
from flask_jwt_extended import create_access_token, create_refresh_token

class UsuariosController:

    def __init__(self) -> None:
        self.model = UsuariosModel

    def crearUsuario(self, data):
        try:
            contrasena = self.__encriptarContrasena(data['contrasena'])
            usuario = self.model(data['nombres'], data['correo'], data['imagen'], contrasena)                                               
            db.session.add(usuario)
            db.session.commit()
            return{
                'data': usuario.convertirJson()
            }
        except Exception as e:
            return{
                'message': 'Internal server error',
                'error': str(e)
            },500

    def iniciarSesion(self, data):
        try:
            usuario = self.model.query.filter_by(correo=data['correo']).first()
            if not usuario:
                return{
                    'message': 'Unauthorized'
                },401
            
            if not self.__comprobarContrasena(usuario.contrasena, data['contrasena']):
                return{
                    'message': 'Unauthorized'
                },401
            access_token = create_access_token(identity={
                "id": usuario.id,
                "correo": usuario.correo
            })
            refresh_token = create_refresh_token(identity={
                "id": usuario.id,
                "correo": usuario.correo
            })
            return{
                'access_token': access_token,
                'refresh_toke': refresh_token
            }, 200

        except Exception as e:
            return{
                'message': 'Internal server error',
                'error': str(e)
            },500

    def  refreshSesion (self, identity):
        try:
            if not identity:
                return{
                    'message': 'Unauthorized'
                },401
            access_token = create_access_token(identity=identity)
            return{
                'access_token': access_token
            },200
        except Exception as e:
            return{
                'message': 'Internal server error',
                'error': str(e)
            },500


    def __comprobarContrasena(self,  contra_hash ,contrasena):
        return check_password_hash( contra_hash, contrasena)


    def __encriptarContrasena(self, contrasena):
        return generate_password_hash(contrasena)

    