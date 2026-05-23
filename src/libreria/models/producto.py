class Producto:
    def __init__(self, nombre, precio, descuento=0):
        self.nombre = nombre
        self.precio = precio
        self.descuento = descuento
        self.precio_final = self.calcular_precio_final()

    def __str__(self):
        return f"Producto(nombre='{self.nombre}', precio={self.precio}, descuento={self.descuento})"
    
    def calcular_precio_final(self):
        if self.descuento > 0:
            return self.precio * (self.descuento / 100)
        return self.precio