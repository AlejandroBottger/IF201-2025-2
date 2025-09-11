class Dispositivo:
    def __init__(self, marca:str, modelo:str):
        self.marca = marca
        self.modelo = modelo

class Smartphone(Dispositivo):
    def __init__(self, marca:str, modelo:str, sistema_operativo:str):
        super().__init__(marca, modelo)
        self.sistema_operativo = sistema_operativo
    
    def info_completa(self):
        return f"Datos del dispositivo:\n Marca: {self.marca}\n Modelo: {self.modelo}\n Sistema Operativo: {self.sistema_operativo}"
    
if __name__ == "__main__":
    phone = Smartphone("Iphone", "17","iOS")
    print(phone.info_completa())