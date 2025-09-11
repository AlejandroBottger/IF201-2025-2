import unittest

class Producto:
    def __init__(self, nombre: str, precio_unitario: float):
        self.nombre = nombre
        self.precio_unitario = precio_unitario
    def calcular_pago(self, cantidad: int)-> float:
        return cantidad * self.precio_unitario
    
class ProductoElectronico(Producto):
    def calcular_pago(self, cantidad: int)-> float:
        if cantidad > 5:
            return super().calcular_pago(cantidad) * 0.9
        else:
            return super().calcular_pago(cantidad)
        
class ProductoAlimentario(Producto):
    def __init__(self, nombre:str, precio_unitario: float, fecha_vencimiento: str):
        super().__init__(nombre, precio_unitario)
        self.fecha_vencimiento = fecha_vencimiento
    
    
    


if __name__ == "__main__":
    elect = ProductoElectronico("Parlante", 2)
    print(elect.calcular_pago(6))
    print(elect.calcular_pago(5))
    alim = ProductoAlimentario("Paneton", 5 ,"2025-12-25")
    print(alim.calcular_pago(4))
    print(alim.calcular_pago(3))