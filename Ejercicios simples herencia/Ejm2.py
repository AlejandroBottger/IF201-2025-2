import unittest
class Vehiculo:
    def __init__(self, marca:str, modelo:str, velocidad_mx: int):
        self.marca = marca
        self.modelo = modelo
        self.velocida_mx = velocidad_mx
    
    def detalles(self):
        return f"Datos del vehiculo:\n Marca: {self.marca}\n Modelo: {self.modelo}\n Velocidad Máx: {self.velocida_mx}"
    
    
class Automovil(Vehiculo):
    def __init__(self, marca:str, modelo:str, velocidad_mx:int, num_puertas: int):
        super().__init__(marca, modelo, velocidad_mx)
        self.num_puertas = num_puertas
    
    
class Motocicleta(Vehiculo):
    def __init__(self, marca:str, modelo:str, velocidad_mx:int, tipo:str):
        super().__init__(marca, modelo, velocidad_mx)
        self.tipo = tipo
        
        
if __name__ == "__main__":
    auto = Automovil("Toyota", "5", 60, 4)
    print(auto.detalles()+ f"Mi auto tiene {auto.num_puertas} puertas")
    moto = Motocicleta("Honda", "10", 120, "deportiva")
    print(moto.detalles() + f"Mi moto es de tipo {moto.tipo}")
     
class TestVehiculo(unittest.TestCase):
    def setUp(self):
        self.veh01 = Automovil("Honda","XRTG", 620, 4)
        self.moto01 = Motocicleta("Mazda", "HOG-RIDER", 500, "deportiva")
        
    def test_compara_velocidad(self):
        self.assertGreater(self.veh01.velocida_mx, self.moto01.velocida_mx)
        
    def test_compara_longitud(self):
        self.assertEqual(len(self.veh01.marca), len(self.moto01.marca))      
        
if __name__ == "__main__":
    unittest.main()