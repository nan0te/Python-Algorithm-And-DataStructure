from Figura import Figura

class Cuadrado(Figura):

    def __init__(self,nombre, color, lado):
        super().__init__(nombre,color)
        self.lado = lado

    def perimetro(self):
        
        perimetro = self.lado + self.lado + self.lado + self.lado
        print('El primetro del cuadrado es: ' , perimetro)

    def area(self):
        area = self.lado * self.lado
        print('El area del cuadrado es: ', area , ' cm cuadrados')
    
    def mostrar(self):
        print('Lados : ', self.lado, ' ', self.area(self), ' ', self.perimetro(self) )
    
    def Mover(self, Dx, Dy):
        print('La figura se mueve : ', Dx, ' en el eje X y ', Dy, ' posiciones en el Eje Y')
