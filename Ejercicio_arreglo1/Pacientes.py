class Paciente:
    def __init__(self,id, nombre, edad, diagnostico, especialidad, costo):
        self.id = id
        self.nombre = nombre
        self.edad = int(edad)
        self.diagnostico = diagnostico
        self.especialidad = especialidad
        self.costo = float(costo)
             
    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.edad} - {self.diagnostico} - {self.especialidad} - ${self.costo:.2f}"
    
    def iniciales(self):
        nombres = self.nombre.split()
        iniciales = ''.join([n[0].upper() + '.' for n in nombres])
        return iniciales
    
    
if __name__ == '__main__':
    pcnt = Paciente("P001","Juan Pérez Gómez",45,"Hipertensión", "Cardiología", 150.00)
    print(pcnt)

    