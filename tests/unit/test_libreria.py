import pytest


from libreria.services.producto_service import ProductoService
from libreria.exceptions import  (PrecioBaseCeroException, ValorNegativoException)

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


