# Clase padre FiguraGeometrica
class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self.__ancho = ancho
        self.__alto = alto

    # Getters y setters
    def get_ancho(self):
        return self.__ancho

    def set_ancho(self, ancho):
        self.__ancho = ancho

    def get_alto(self):
        return self.__alto

    def set_alto(self, alto):
        self.__alto = alto

    def __str__(self):
        return f"FiguraGeometrica [ancho: {self.__ancho}, alto: {self.__alto}]"


# Clase padre Color
class Color:
    def __init__(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def __str__(self):
        return f"Color [color: {self.__color}]"


# Clase hija Rectangulo
class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, ancho, alto, color):
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

    def area(self):
        return self.get_ancho() * self.get_alto()

    def __str__(self):
        return f"Rectángulo [ancho: {self.get_ancho()}, alto: {self.get_alto()}, color: {self.get_color()}, área: {self.area()}]"


# Clase hija Cuadrado
class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def area(self):
        return self.get_ancho() ** 2

    def __str__(self):
        return f"Cuadrado [lado: {self.get_ancho()}, color: {self.get_color()}, área: {self.area()}]"


# Prueba del programa
if __name__ == "__main__":
    rectangulo = Rectangulo(5, 3, "rojo")
    cuadrado = Cuadrado(4, "azul")

    print(rectangulo)
    print(cuadrado)
