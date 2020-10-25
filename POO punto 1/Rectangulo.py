from Figura import Figura

class Rectangulo(Figura):
    def __init__(self, nombre, color, ladoa, ladob):
        super().__init__(nombre, color)
        self.ladoA = ladoa
        self.ladoB = ladob
    
    def perimetro(self):
        perimetro = self.ladoA + self.ladoA + self.ladoB + self.ladoB
        return perimetro
    
    def area(self):
        area = self.ladoA * self.ladoB
        return area

    def mostrar(self):
        print('Lado 1 = ', self.ladoA, '. Lado 2 = ', self.ladoB)

    def mover(self,Dx, Dy):
        print('La figura se mueve : ', Dx, ' en el eje X y ', Dy, ' posiciones en el Eje Y')