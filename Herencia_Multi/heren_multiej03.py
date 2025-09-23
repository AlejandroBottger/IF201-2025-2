import unittest

class Reserva:
    def __init__(self, cliente:str, noches:int):
        self.cliente = cliente
        self.noches = noches
    def mostrar_info(self):
        return f" Estimado {self.cliente}\n Le quedan {self.noches} noches"
     

class HabitacionEstandar(Reserva):
    def __init__(self, cliente:str, noches:int, precio_noche: float):
        super().__init__(cliente, noches)
        self.precio_noche = precio_noche
    def calcular_total(self) -> float:
        return self.precio_noche * self.noches
    def mostrar_info(self) -> str:
        return super().mostrar_info() + f"\n Total a pagar: {self.calcular_total()}"
    
class Suite(Reserva):
    def __init__(self, cliente:str, noches:int, precio_noche:float):
        super().__init__(cliente, noches)
        self.precio_noche = precio_noche
    def calcular_total(self) -> float:
        return self.precio_noche * self.noches
    def mostrar_info(self) -> str:
        return super().mostrar_info() + f"\n Total a pagar: {self.calcular_total()}"

class VIP:
    def __init__(self, descuento: float):
        self.descuento = descuento
    def aplicar_descuento(self, total:float) -> float:
        return total * (1 - self.descuento)
    def mostrar_info_vip(self):
        return f"Descuento VIP aplicado: {self.descuento * 100}% "

class ReservaEstandarVIP(HabitacionEstandar, VIP):
    def __init__(self, cliente:str, noches:int, precio_noche:float, descuento:float):
        super().__init__(cliente, noches, precio_noche)
        VIP.__init__(self, descuento)
    def mostrar_info(self):
        return super().mostrar_info()

class ReservaSuiteVIP(Suite, VIP):
    def __init__(self, cliente, noches, precio_noche, descuento:float):
        super().__init__(cliente, noches, precio_noche)
        VIP.__init__(self,descuento)
    def mostrar_info(self):
        return super().mostrar_info()
    
    
class TestPruebaReservaHerencia(unittest.TestCase):
    def setUp(self):
        self.vip = VIP(25.00)
        self.hest = HabitacionEstandar("Pepito", 4, 120.00)
        self.st = Suite("Ana", 3, 180.00)
        self.retvp = ReservaEstandarVIP("Ale", 2, 60.00, 0.45)
        self.restvp = ReservaSuiteVIP("Ricky", 4, 240.00, 0.50)
        
        
    def test_texto_VIP(self):
        self.assertIn("Descuento", self.vip.mostrar_info_vip())
    def test_HabiEstandar(self):
        self.assertIn(str(self.hest.noches), self.hest.mostrar_info())
    def test_Suite(self):
        self.assertIn(str(self.st.noches), self.st.mostrar_info())
    def test_diferente_descuento(self):
       self.assertNotEqual(self.retvp.descuento, self.restvp.descuento)
       
       
       
if __name__ == "__main__":
     unittest.main()