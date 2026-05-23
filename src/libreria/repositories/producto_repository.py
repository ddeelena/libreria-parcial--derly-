class ProductoRepository:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)


    def obtener_productos(self):
        return self.productos
    
    def obtener_producto_por_nombre(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return None