class Socio:
    def __init__(self, id, nombre, edad, plan, mensualidad):
        self.id = id
        self.nombre = nombre
        self.edad = int(edad)
        self.plan = plan
        self.mensualidad = float(mensualidad)

class ArchivoSocios:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.arreglo = []

    def abrir(self):
        with open(self.nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                partes = linea.strip().split(';')
                socio = Socio(*partes)
                self.arreglo.append(socio)
        return self.arreglo