from empleado import Empleado
class Empleado_tiempo_completo(Empleado):
    def __init__(self, nombre: str, salario_base: float, bono:float):
        super().__init__(nombre, salario_base)
        self.bono = bono 
        
    def calcular_salario(self) -> float:
        return super().calcular_salario() + self.bono

        
if __name__ == "__main__":
    emp = Empleado_tiempo_completo("Juan", 2000, 500)
    print(f"El salario calculado es :{emp.calcular_salario()}")
    emp.mostrar_información()