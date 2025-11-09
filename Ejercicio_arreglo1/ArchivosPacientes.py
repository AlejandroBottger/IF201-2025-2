from Pacientes import Paciente

class Archivo:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.arreglo = []
        
    def abrir(self):
        self.arreglo.clear()
        with open(self.nombre_archivo, 'r', encoding='UTF-8') as archivo:
            for linea in archivo:
                partes = linea.strip().split(';')
                paciente = Paciente(partes[0], partes[1], partes[2], partes[3], partes[4],partes[5])
                self.arreglo.append(paciente)
            

    def __str__(self):
        salida = ""
        for emp in self.arreglo:
            salida += str(emp) + "\n"
        return salida
    
    def cerrar(self):
        pass
    
    def mostrar(self):
        return self.arreglo
    
    def paciente_mayor_costo(self,lista):
        return max(lista,key = lambda p:p.costo)
    
    def paciente_menor_costo(self,lista):
        return min(lista, key= lambda p:p.costo)
    
    def promedio_por_especialidad(self,lista):
        dicc = {}
        for p in lista:
            if p.especialidad not in dicc:
                dicc[p.especialidad] = []
            dicc[p.especialidad].append(p.costo)
        return {esp: sum(costos)/len(costos) for esp, costos in dicc.items()}
    
    def especialidad_menor_promedio(self,diccionario):
        return min(diccionario, key = diccionario.get)
    
    
if __name__ == '__main__':
    oArch = Archivo('empleados.txt') 
    
    oArch.abrir()
    print(oArch)