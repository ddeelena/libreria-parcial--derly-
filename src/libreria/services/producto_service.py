
from libreria.exceptions.precio_base_cero import PrecioBaseCeroException
from libreria.models.producto import Producto
from libreria.exceptions.valor_negativo import ValorNegativoException
from libreria.repositories.producto_repository import ProductoRepository
from libreria.exceptions.descuento_mayor import DescuentoMayorException

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
    
    def aplicar_descuento(self, producto, descuento):

        self.validar_descuento(descuento)

        producto.descuento = descuento
        producto.precio_final = producto.calcular_precio_final()


    def validar_descuento(self, descuento):

        if descuento < 0:
            raise ValorNegativoException(
                "El descuento no puede ser negativo."
            )

        if descuento > 40:
            raise DescuentoMayorException(
                "El descuento no puede ser mayor al 40%"
            )