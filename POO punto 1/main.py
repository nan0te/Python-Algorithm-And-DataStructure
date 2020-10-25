# TRABAJO 2DO CUATRIMESTRE

from Triangulo import Triangulo
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from Circulo import Circulo

triangle = Triangulo('Triangulito', 'Violeta', 4, 8)
print('Area del triangulito: ', triangle.area() )
triangle.Mostrar()

square = Cuadrado('Cuadradito', 'Purple', 10)
print('Perimetro del cuadradito: ', square.perimetro() )

rectangle =  Rectangulo('Rectangulito', 'Violet', 10, 5)
rectangle.mostrar()
rectangle.mover('4', '6')

circle = Circulo('Circulito', 'Verde', 7)
circle.mostrar()





