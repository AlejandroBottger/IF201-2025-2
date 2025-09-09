import unittest
class Vehiculo:
    def __init__(self, marca: str, modelo:str):
        self.marca = marca
        self.modelo = modelo 
    def mostrar_info(self):
        return f"Datos del Vehiculo\n Marca:{self.marca}\n Modelo:{self.modelo}"
    
class Automovil(Vehiculo):
    def __init__(self, marca:str, modelo:str, num_puertas: int):
        super().__init__(marca, modelo)
        self.num_puertas = num_puertas
    
    def es_deportivo(self) -> bool:
        return (self.num_puertas == 2)
    
class TestPruebaAutomovil(unittest.TestCase):
    def setUp(self): #definamos objetos en las pruebas
        self.auto1 = Automovil("Mazda", "3", 4)
        self.auto2 = Automovil("Ferrari", "Z", 2)

    def test_auto_no_deportivo(self):
        self.assertFalse(self.auto1.es_deportivo())
    
    def test_auto_deportivo(self):
        self.assertTrue(self.auto2.es_deportivo())
    
    def test_auto_deportivo_2(self):                       #Otras pruebas
        self.assertEqual(self.auto2.es_deportivo(), True)  #Comparacion con el Equal

    def test_auto_deportivo_3(self):                       #Otras pruebas
        self.assertLess(self.auto2.num_puertas,3)

if __name__ == "__main__":
    #unittest.main() #No complia con lo de abajo, solo uno a la vez
    #Prueba clase Automovil

    auto3 = Automovil("Honda", "Accord", 3)
    if auto3.es_deportivo():
        print(auto3.mostrar_info() + '\n(Auto Deportivo)')
    else:
        print(auto3.mostrar_info() + '\n (Auto sedán)')