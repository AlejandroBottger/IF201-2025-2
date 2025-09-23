import unittest


class Vehículo:
    def __init__(self, marca:str, modelo:str):
        self.marca = marca
        self.modelo = modelo
    def mostrar_info(self):
        return f"Marca: {self.marca}\n Modelo:{self.modelo}"
    
class Coche(Vehículo):
    def __init__(self, marca:str, modelo:str, puertas:int):
        super().__init__(marca, modelo)
        self.puertas = puertas
    def mostrar_info(self):
        return super().mostrar_info() + f", Puertas: {self.puertas}"

class Motocicleta(Vehículo):
    def __init__(self, marca:str, modelo:str, cilindrada:int):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada
    def mostrar_info(self):
        return super().mostrar_info() + f", Cilindrada: {self.cilindrada}"
class Electrico:
    def __init__(self, autonomia:int):
        self.autonomia = autonomia
    def mostrar_info_electrico(self):
        return f"Autonomia: {self.autonomia}"

class CocheElectrico(Coche, Electrico):
    def __init__(self, marca:str, modelo:str, puertas:int, autonomia:int):
        super().__init__(marca, modelo, puertas)
        Electrico.__init__(self, autonomia)
    def mostrar_info(self):
        return super().mostrar_info() + f", La autonomia en: {Electrico.mostrar_info_electrico(self)}"    
    
class MotoElectrica(Motocicleta, Electrico):
    def __init__(self, marca:str, modelo:str, cilindrada:int, autonomia:int):
        super().__init__(marca, modelo, cilindrada)
        Electrico.__init__(self,autonomia)
    def mostrar_info(self):
        return super().mostrar_info() + f"La autonomia en: {Electrico.mostrar_info_electrico(self)}"


class TestPruebaVehículosHerencia(unittest.TestCase):
    def setUp(self):
        self.electric = Electrico(100) #el 100 es autonomia
        self.ch = Coche("BMW", "Silver", 4)
        self.mt = Motocicleta("Honda", "LRQ", 250)
        self.chel = CocheElectrico("Tesla", "DX", 2, 80)
        self.mtel = MotoElectrica("GreenLine", "yeah", 85, 75)
    
    def test_texto_electrico(self):
        self.assertIn("Autonomia", self.electric.mostrar_info_electrico())
    def test_electrico(self):
        self.assertIn(str(self.ch.puertas),self.ch.mostrar_info() )
    def test_motocicleta(self):
        self.assertIn(str(self.mt.cilindrada),self.mt.mostrar_info() )    
    def test_diferente_electrico(self):
        self.assertNotEqual(self.chel.autonomia, self.mtel.autonomia)
        
        
if __name__ == "__main__":
    unittest.main()