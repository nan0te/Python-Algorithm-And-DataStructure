from Figura import Figura

class Circulo(Figura):
    def __init__(self, nombre, color, radio):
        super().__init__(nombre, color)
        self.__Name = nombre
        self.__Color = color
        self.__radio = radio
    
    def perimetro(self):
        perimetro = 2 * 3.14 * self.__radio
        return perimetro
    
    def area(self):
        area = 3.14 * (self.__radio * self.__radio)
        return area

    def mostrar(self):
        print('Radio = ', self.__radio, ' Area del circulo: ', self.area(), '. Perimetro del circulo: ', self.perimetro()  )

    def mover(self, Dx, Dy):
        print('La figura se mueve : ', Dx, ' en el eje X y ', Dy, ' posiciones en el Eje Y')

    def getName(self):
        return self.__Name
        