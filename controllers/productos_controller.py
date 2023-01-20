from models.productos_model import ProductosModel
from models.categorias_productos import CategoriasProductosModel
from db import db

class ProductosController:

    def crearProducto(self, data):
        try:
            producto = ProductosModel(data['nombre'], data['precio'])
            db.session.add(producto)
            db.session.commit()

            nuevas_categorias = []
            for categoria in data['categorias']:
                nueva_categoria  = CategoriasProductosModel(producto.id, categoria['categoria_id'])
                nuevas_categorias.append(nueva_categoria)
            db.session.add_all(nuevas_categorias)
            db.session.commit()
            return {
                'data': producto.convertirJson()
            },201
        except Exception as e:
            # Borramos lo que ya se habia almcenado
            db.session.rollback()
            return {
                'message': 'Internal server error',
                'error': str(e)
            }

    def listarProductos(self):
        productos = ProductosModel.query.all()
        response = []
        for producto in productos:
            response.append({
                'id': producto.id,
                'nombre': producto.nombre,
                'precio': producto.precio
            })
        return {
            'data': response
        }
    def eliminarProducto(self, producto_id):
        try:
            producto = ProductosModel.query.filter_by(id=producto_id).first()
            producto.estado = False
            db.session.commit()
            print(producto)
            return{
                'message': 'Producto eliminado correctamente'
            }
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Internal server error',
                'error': str(e)
            }
    
    def actualizarProducto(self, producto_id, data):
        try:
            producto = ProductosModel.query.filter_by(id=producto_id).first()
            producto.nombre = data['nombre']
            producto.precio = data['precio']
            # En caso de PUT solo usar commit
            db.session.commit()
            return {
                'data': producto.convertirJson()
            },201
        except Exception as e:
            db.session.rolback()
            return {
                'message': 'Internal server error',
                'error': str(e)
            },500

    def buscarProducto(self, precio):
        try:
            productos = ProductosModel.query.filter_by(precio=precio).all()
            response = []
            for producto in productos:
                response.append(producto.convertirJson())
            return{
                'data': response
            }
        except Exception as e:
            db.session.rolback()
            return {
                'message': 'Internal server error',
                'error': str(e)
            },500