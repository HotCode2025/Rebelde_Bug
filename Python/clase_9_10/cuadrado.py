# 12.3 Creamos la clase hija Cuadrado

from color import Color
from figuraGeometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, ancho, alto, color):
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

    def area(self):
        return self.ancho * self.alto
    
    def __str__(self):
        return f"Ancho: {self.ancho}, Alto: {self.alto}, Color: {self.color}"
