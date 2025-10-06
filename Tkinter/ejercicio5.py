from abc import ABC, abstractmethod

class UnidadHospitalaria(ABC):
    
    def __init__(self, id: str, nombre: str, capacidad_maxima: int):
        self.id = id
        self.nombre = nombre
        self.capacidad_maxima = capacidad_maxima
        
    @abstractmethod
    def operar(self):
        pass

class AtencionPacientes(UnidadHospitalaria):
    def __init__(self, id, nombre, capacidad_maxima, num_pacientes: int):
        UnidadHospitalaria.__init__(self, id, nombre, capacidad_maxima)
        self.num_pacientes = num_pacientes
        
    def admitir_pacientes(self, n):
        if self.num_pacientes + n > self.capacidad_maxima:
            return f'{self.nombre}: No se puede superar la capacidad máxima: {self.capacidad_maxima}'
        else:
            self.num_pacientes += n
            return f'{self.nombre}: Admitidos {n} pacientes. Total: {self.num_pacientes}'
            
    def dar_alta_pacientes(self, n):
        if self.num_pacientes - n < 0:
            return f'{self.nombre}: No se puede dar de alta a una cantidad mayor al numero de pacientes: {self.num_pacientes}'
        else:
            self.num_pacientes -= n
    
class GestionEquipos(UnidadHospitalaria):
    def __init__(self, id, nombre, capacidad_maxima, equipos_medicos: int):
        UnidadHospitalaria.__init__(self, id, nombre, capacidad_maxima)
        self.equipos_medicos = equipos_medicos
    
    def asignar_equipo(self, equipo):
        if self.equipos_medicos + equipo > self.capacidad_maxima:
            return f'{self.nombre}: No se puede superar la capacidad máxima: {self.capacidad_maxima}'
        else:
            self.equipos_medicos += equipo
            return f'{self.nombre}: Admitidos {equipo} equipos. Total: {self.equipos_medicos}'
    def retirar_equipo(self, equipo):
        if self.equipos_medicos - equipo < 0:
            return f'{self.nombre}: No se puede retirar una cantidad mayor al numero de equipos: {self.equipos_medicos}'
        else:
            self.equipos_medicos -= equipo

class UnidadMixta(AtencionPacientes, GestionEquipos):
    def __init__(self, id, nombre, capacidad_maxima, num_pacientes, equipos_medicos):
        super().__init__(id, nombre, capacidad_maxima, num_pacientes)
        GestionEquipos.__init__(self, id, nombre, capacidad_maxima, equipos_medicos)

    def operar(self):
        self.capacidad_maxima = self.num_pacientes + self.equipos_medicos

class UnidadEmergencia(UnidadMixta):
    def __init__(self, id, nombre, capacidad_maxima, num_pacientes, equipos_medicos, nivel_oxigeno: float):
        super().__init__(id, nombre, capacidad_maxima, num_pacientes, equipos_medicos)
        self.nivel_oxigeno = nivel_oxigeno/100
        
    def operar(self):
        if self.nivel_oxigeno >= 0.1:
            self.nivel_oxigeno -= (0.005*float(self.num_pacientes))
            return f'{self.nombre}: Nivel de oxigeno al: {self.nivel_oxigeno*100}%'
        else:
            return f'{self.nombre}: No se puede operar debido a bajos niveles de oxigeno: {self.nivel_oxigeno*100}%'
    
class UCI(UnidadMixta):
    def __init__(self, id, nombre, capacidad_maxima, num_pacientes, equipos_medicos, energia_respaldo: float, modo: str):
        super().__init__(id, nombre, capacidad_maxima, num_pacientes, equipos_medicos)
        self.energia_respaldo = energia_respaldo
        self.modo = modo
        
    def operar(self):
        if self.modo == 'Eléctrico':
            self.energia_respaldo -= (0.007 * float(self.num_pacientes))
            
        if self.energia_respaldo < 20.0:
            self.modo = 'Generador'
            return f'{self.nombre}: Bajos niveles de energía {self.energia_respaldo}%, cambiando a modo Generador'
        else:
            return f'{self.nombre}: Energia de respaldo al {self.energia_respaldo}%'
            

if __name__ == '__main__':
    
    ue = UnidadEmergencia('01', 'Auxliar', 50, 30, 10, 100)
    uci = UCI('02', 'TEST', 80, 40, 20, 100, 'Eléctrico')
    ue1 = UnidadEmergencia('03', 'Cayetano', 100, 20, 20, 70)
    
    print(ue.admitir_pacientes(30))
    print(uci.asignar_equipo(10))
    print(ue1.operar())
    print(ue.operar())