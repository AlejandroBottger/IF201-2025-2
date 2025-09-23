from clases_lista import Cola

from herencia_multiple_telefono_intgnt import DispConectividad 
from herencia_multiple_telefono_intgnt import DispElectronico


class Smartphone(DispElectronico, DispConectividad):
    def __init__(self):
        DispElectronico.__init__(self)
        DispConectividad.__init__(self)
        self.descargas = Cola()
        # Inicializamos con los 5 elementos pedidos
        for item in ["Video", "Juego", "Libro", "App", "Música"]:
            self.descargas.encolar(item)

    def usar_app(self):
        if self.encendido:
            print("Usando una aplicación en el smartphone...")
        else:
            print("El teléfono está apagado. No se puede usar la app.")

    def conectar_wifi(self, tipo_conexion):
        if self.encendido:
            self.conectar(tipo_conexion)
        else:
            print("No se puede conectar. El teléfono está apagado.")

    def descargar(self):
        if not self.encendido:
            print("No se puede descargar. El teléfono está apagado.")
            return
        if not self.red_activa:
            print("No se puede descargar. No hay conexión a internet.")
            return
        archivo = self.descargas.desencolar()
        if archivo:
            print(f"Descargando: {archivo}...")
        else:
            print("No hay más descargas disponibles.")