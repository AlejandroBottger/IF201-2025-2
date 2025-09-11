import unittest
class Empleado:
    def __init__(self, nombre:str, edad:int, salario:float):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
    def calcular_bono(self):
        return self.salario * 0.1
    
class Gerente(Empleado):
    def __init__(self, nombre:str, edad:int, salario: float, departamento:str):
        super().__init__(nombre, edad, salario)
        self.departamento = departamento
        
    def calcular_bono(self):
        return self.salario * 0.2
    
    
 
    
class TestEmpleado(unittest.TestCase):
    def setUp(self):
        self.emp01 = Empleado("Pepe", 20, 3000.00)
        self.gerent01 = Gerente("Anastasia", 33, 5000.00, "Finanzas")
    
    def test_compara_salarios(self):
        self.assertLess(self.emp01.salario, self.gerent01.salario)
        
    def test_compara_bono(self):
        self.assertEqual(self.emp01.calcular_bono(), 300)
        self.assertEqual(self.gerent01.calcular_bono(), 1000)
        
    def test_nombre(self):
        self.assertTrue(len(self.gerent01.nombre) > len(self.emp01.nombre))
    
if __name__ == "__main__":
    unittest.main()   
    