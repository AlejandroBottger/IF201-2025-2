class DispElectronico:
    def __init__(self):
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print("El dispositivo se ha encendido.")
        else:
            print("El dispositivo ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print("El dispositivo se ha apagado.")
        else:
            print("El dispositivo ya está apagado.")

class DispConectividad:
    def __init__(self):
        self.red_activa = None

    def conectar(self, tipo_conexion):
        if tipo_conexion in ["wi-fi", "plan de datos", "por cable"]:
            self.red_activa = tipo_conexion
            print(f"Conectado a la red {tipo_conexion}.")
        else:
            print("Tipo de conexión no válido.")

    def desconectar(self):
        if self.red_activa:
            print(f"Desconectado de la red {self.red_activa}.")
            self.red_activa = None
        else:
            print("No hay ninguna conexión activa.")

class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)  # FIFO
        else:
            return None

    def esta_vacia(self):
        return len(self.items) == 0

