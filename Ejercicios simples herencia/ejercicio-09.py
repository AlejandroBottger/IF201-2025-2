class Vehiculo:
    def __init__(self, velocidad_maxima: float):
        self.velocidad_maxima = velocidad_maxima
    def obtener_velocidad_maxima(self):
        return self.velocidad_maxima
    
class Automovil(Vehiculo):
    def __init__(self, velocidad_maxima: float, numero_puertas: int):
        super().__init__(velocidad_maxima)
        self.numero_puertas = numero_puertas
        
class Motocicleta(Vehiculo):
    def __init__(self, velocidad_maxima:float, cilindrada:float):
        super().__init__(velocidad_maxima)
        self.cilindrada = cilindrada
    def es_alta_cilindrada(self):
        return self.cilindrada >=500
    
if __name__== "__main__":
    auto1 = Automovil(180, 4)
    print("Automovil --> Velocidad máxima:", auto1.obtener_velocidad_maxima(), "km/h")
    print("Número de puertas:", auto1.numero_puertas)

    moto1 = Motocicleta(220, 150)
    print("\nMotocicleta 150cc -> Velocidad máxima:", moto1.obtener_velocidad_maxima(), "km/h")
    print("¿Es alta cilindrada?", moto1.es_alta_cilindrada())

    moto2 = Motocicleta(280, 650)
    print("\nMotocicleta 650cc -> Velocidad máxima:", moto2.obtener_velocidad_maxima(), "km/h")
    print("¿Es alta cilindrada?", moto2.es_alta_cilindrada())