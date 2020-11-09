from Figura import Figura

class Cuadrado(Figura):

    def __init__(self,nombre, color, lado):
        super().__init__(nombre,color)
        self.__Name = nombre
        self.__Color = color
        self.__lado = lado

    def perimetro(self):
        
        perimetro = self.__lado + self.__lado + self.__lado + self.__lado
        print('El primetro del cuadrado es: ' , perimetro)

    def area(self):
        area = self.__lado * self.__lado
        print('El area del cuadrado es: ', area , ' cm cuadrados')
    
    def mostrar(self):
        print('Lados : ', self.__lado, ' ', self.area(self), ' ', self.perimetro(self) )
    
    def Mover(self, Dx, Dy):
        print('La figura se mueve : ', Dx, ' en el eje X y ', Dy, ' posiciones en el Eje Y')

    def getName(self):
        return self.__Name