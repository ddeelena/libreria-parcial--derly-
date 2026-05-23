import pytest


from libreria.services.producto_service import ProductoService
from libreria.exceptions.precio_base_cero import  PrecioBaseCeroException
from libreria.exceptions.valor_negativo import ValorNegativoException
from libreria.exceptions.descuento_mayor import DescuentoMayorException

@pytest.fixture
def producto_service():
    return ProductoService()


# Regla numero 1: Un producto tiene nombre y precio base. El precio base debe ser mayor que cero. 

def test_crear_producto(producto_service):
    producto_service.crear_producto(nombre="Libro A", precio=50000)
    assert producto_service.obtener_producto("Libro A").nombre == "Libro A"
    assert producto_service.obtener_producto("Libro A").precio == 50000

def test_producto_con_precio_cero(producto_service):
    with pytest.raises(PrecioBaseCeroException):
        producto_service.crear_producto(nombre="Cuaderno", precio=0.0)

def test_producto_con_precio_negativo(producto_service):
    with pytest.raises(ValorNegativoException):
        producto_service.crear_producto(nombre="Lápiz", precio=-1000.0)


# Regla numero 2: Un producto puede tener un descuento, el cual se aplica al precio base para obtener el precio final. El descuento no puede ser negativo ni mayor que el precio base.

def test_producto_con_descuento(producto_service):
    producto_service.crear_producto(nombre="Libro B", precio=50000)
    producto = producto_service.obtener_producto("Libro B")
    producto_service.aplicar_descuento(producto, 20)

    assert producto.descuento == 20
    assert producto.precio_final == 40000

def test_producto_con_descuento_cero(producto_service):
    producto_service.crear_producto(nombre="Libro C", precio=50000)
    producto = producto_service.obtener_producto("Libro C")
    producto_service.aplicar_descuento(producto, 0)

    assert producto.descuento == 0
    assert producto.precio_final == 50000

def test_producto_con_descuento_cuarenta_por_ciento(producto_service):
    with pytest.raises(DescuentoMayorException):
        producto_service.crear_producto(nombre="Libro D", precio=50000)
        producto = producto_service.obtener_producto("Libro D")
        producto_service.aplicar_descuento(producto, 45)
        