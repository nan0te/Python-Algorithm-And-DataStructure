from Figura import Figura

class Rectangulo(Figura):
    def __init__(self, nombre, color, ladoa, ladob):
        super().__init__(nombre, color)
        self.__Name = nombre
        self.__Color = color
        self.__ladoA = ladoa
        self.__ladoB = ladob
    
    def perimetro(self):
        perimetro = self.__ladoA + self.__ladoA + self.__ladoB + self.__ladoB
        return perimetro
    
    def area(self):
        area = self.__ladoA * self.__ladoB
        return area

    def mostrar(self):
        print('Lado 1 = ', self.__ladoA, '. Lado 2 = ', self.__ladoB)

    def mover(self,Dx, Dy):
        print('La figura se mueve : ', Dx, ' en el eje X y ', Dy, ' posiciones en el Eje Y')
    
    def getName(self):
        return self.__Name