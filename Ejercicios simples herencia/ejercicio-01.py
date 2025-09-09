class Persona:
    def __init__(self, nombre:str, edad:int):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return (f"Hola, soy {self.nombre}, y tengo {self.edad} años")
    
class Estudiante(Persona):
    def __init__(self, nombre: str, edad: int, carrera: str):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def presentarse(self):
        return super().presentarse() + f" y estudio la carrera {self.carrera}"

if __name__ == "__main__":
    oEst = Estudiante("Juan", 21, "Ing. Informática")
    print(oEst.presentarse())
