

class ProductosController:
    # Self = nos permite acceder a los methd y prop que estan dentro del objs
    def listarProductos(self):
        productos = [
            {
                'nombre' : 'Zapatillas nike',
                'precio': 200.00,
                'talla': 42,
            },
            {
                'nombre' : 'Zapatillas Pumba',
                'precio': 150.00,
                'talla': 41,
            },
        ]
        return productos