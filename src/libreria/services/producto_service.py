
from libreria.exceptions.precio_base_cero import PrecioBaseCeroException
from libreria.models.producto import Producto
from libreria.exceptions.valor_negativo import ValorNegativoException
from libreria.repositories.producto_repository import ProductoRepository

class ProductoService:
    def __init__(self):
        self.productos = {}
        self.repository = ProductoRepository()

    def crear_producto(self, nombre, precio):
        if precio == 0:
            raise PrecioBaseCeroException("El precio base debe ser mayor que cero.")
        if precio < 0:
            raise ValorNegativoException("El precio no puede ser negativo.")
        producto = Producto(nombre, precio)
        self.repository.agregar_producto(producto)

    def obtener_producto(self, nombre):
        return self.repository.obtener_producto_por_nombre(nombre)