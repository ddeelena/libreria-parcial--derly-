
from libreria.exceptions.precio_base_cero import PrecioBaseCeroException
from libreria.models.producto import Producto
from libreria.exceptions.valor_negativo import ValorNegativoException

class ProductoService:
    def __init__(self):
        self.productos = {}

    def crear_producto(self, nombre, precio):
        if precio == 0:
            raise PrecioBaseCeroException("El precio base debe ser mayor que cero.")
        if precio < 0:
            raise ValorNegativoException("El precio no puede ser negativo.")
        producto = Producto(nombre, precio)
        self.productos[nombre] = producto

    def obtener_producto(self, nombre):
        return self.productos.get(nombre)