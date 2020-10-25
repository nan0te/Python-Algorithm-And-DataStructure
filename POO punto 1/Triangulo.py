from Figura import Figura
import math


class Triangulo(Figura):

    def __init__(self, nombre, color, base, altura):
        super().__init__(nombre, color)
        self.base =  base
        self.altura = altura
    
    def perimetro(self):
        rbase = math.pow( self.base, 2)
        raltura = math.pow( self.base, 2)
        catetos = rbase + raltura
        result = math.sqrt(catetos)

        return result + rbase + raltura

    def area(self):
        result = self.base * self.altura / 2
        return result

    def Mostrar(self):
        print('Altura del triangulo : ', self.altura, ' - Base del triangulo : ', self.base)
    
    def Mover(self, Dx, Dy):
        print('La figura se mueve : ', Dx, ' en el eje X y ', Dy, ' posiciones en el Eje Y')




