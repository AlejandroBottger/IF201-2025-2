from abc import ABC, abstractmethod #Módulo de clases abstractas 
class Empleado(ABC):
    def __init__(self, nombre: str, salario_base: float): #__init_ : creador de objetos
        self.nombre = nombre #self.X : atributo dentro de la clase
        self.salario_base = salario_base
        
    
    def calcular_salario(self) -> float:
        # Debe ser implementado en las clases derivadas
        return self.salario_base
       
    def mostrar_información(self):
        print(f"Empleado: {self.nombre} | Salario base: {self.salario_base}") 
       
if __name__ == "__main__":
    obj = Empleado("Juan", 1000)   
    obj.mostrar_información()
        
        