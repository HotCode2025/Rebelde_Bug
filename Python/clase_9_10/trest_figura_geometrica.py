# 12.4 Creamos la clase para testear nuestro código
# 12.5 Explicación paso a paso con Debug
# 12.6 Método MRO: Method Resolution Order
# 12.7 Tareas: explicado en diagrama de clases, ejercicio Rectángulo
#13.1 Validaciones en atributos
# 13.2 Método encapsulado y setter
# 13.3 Explicación de validaciones setter
# 13.5 Atributo Read-only y método mro

from cuadrado import Cuadrado
from rectangulo import Rectangulo
from figuraGeometrica import FiguraGeometrica

print("Creando un objeto de la clase Cuadrado".center(20, "-"))
cuadrado1 = Cuadrado(5, 5, "rojo")
# podemos modificar los atributos usando los setters
# cuadrado1.ancho = 10
# cuadrado1.alto = 10
print("Ancho:", cuadrado1.ancho)
print("Alto:", cuadrado1.alto)
print("Color:", cuadrado1.color)
print("El área del cuadrado es:", cuadrado1.area())

# MRO = Method Resolution Order
print(Cuadrado.mro())


print(cuadrado1)  # Llama al método __str__() de la clase Cuadrado

print("Creando un objeto de la clase Rectángulo".center(20, "-"))
rectangulo1 = Rectangulo(4, 6, "azul")
# podemos modificar los atributos usando los setters
# rectangulo1.ancho = 12
# rectangulo1.alto = 8
print("Ancho:", rectangulo1.ancho)
print("Alto:", rectangulo1.alto)
print("Color:", rectangulo1.color)
print("El área del rectángulo es:", rectangulo1.area())

# figura1 = FiguraGeometrica(3, 4)  # Esto generará un error no se puede instanciar una clase abstracta

print(Cuadrado.mro())
