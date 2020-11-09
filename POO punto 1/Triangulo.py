from Figura import Figura
import math


class Triangulo(Figura):

    def __init__(self, nombre, color, base, altura):
        super().__init__(nombre, color)
        self.__Name = nombre
        self.__Color = color
        self.__base =  base
        self.__altura = altura
    
    def perimetro(self):
        rbase = math.pow( self.__base, 2)
        raltura = math.pow( self.__base, 2)
        catetos = rbase + raltura
        result = math.sqrt(catetos)

        return result + rbase + raltura

    def area(self):
        result = self.__base * self.__altura / 2
        return result

    def Mostrar(self):
        print('Altura del triangulo : ', __, ' - Base del triangulo : ', self.__base)
    
    def Mover(self, Dx, Dy):
        print('La figura se mueve : ', Dx, ' en el eje X y ', Dy, ' posiciones en el Eje Y')

    def getName(self):
        return self.__Name




