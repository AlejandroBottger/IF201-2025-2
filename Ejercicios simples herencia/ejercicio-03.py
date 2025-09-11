class Figura:
    def area(self):
        return 0
     
class Rectángulo(Figura):
    def __init__(self,base:int, altura:int):
        
        self.base = base
        self.altura = altura
        
    def area(self):
        return f"El área sería: " + str(self.base * self.altura)
     
if __name__ == "__main__":
    Area_real = Rectángulo(2, 3)
    print(Area_real.area())