import Triangulo from Triangulo
import Circulo from Circulo
import Cuadrado from Cuadrado
import Rectangulo from Rectangulo

class ManejadorFiguras:
    listaFiguras = []

    def nuevoTriangulo(self, name, color, base, altura):
        triangle = Triangulo(name, color, base, altura)
        self.listaFiguras.append(triangle)

    def nuevoCirculo(self, name, color, radio):
        circle = Circulo(name, color, radio)
        self.listaFiguras.append(circle)
    
    def nuevoCuadrado(self, name, color, lado):
        square = Cuadrado(name, color, lado)
        self.listaFiguras.append(square)
    
    def nuevoRectangulo(self, name, color, ladoa, ladob):
        rectangle = Rectangulo(name, color, ladoa, ladob)
        self.listaFiguras.append(rectangle)
    
    def imprimirFiguras(self):

        for figura in self.listaFiguras:
            figura.mostrar()

    def buscarFigura(self, name):
        for figura in self.listaFiguras:
            if name == figura.getName():
                figura.mostrar()
    
    def eliminarFigura(self, name):
        position = 0
         for figura in self.listaFiguras:
            if name == figura.getName():
                figura.pop(position)
            position = position + 1
    

    

    