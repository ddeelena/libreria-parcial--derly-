class Producto:
    def __init__(self, nombre, precio, descuento=0):
        self.nombre = nombre
        self.precio = precio
        self.descuento = descuento

    def __str__(self):
        return f"Producto(nombre='{self.nombre}', precio={self.precio}, descuento={self.descuento})"