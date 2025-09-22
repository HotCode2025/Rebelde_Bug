# Ejercicio: Class Cubo
# Crear la clase llamada Cubo con los atributos: ancho, alto y profundidad.
# Con un metodo calcular_volumen() que tendrá la fórmula:
# volumen = ancho * altura * profundidad
# Que el usuario ingrese los datos


class Cubo:
    def __init__(self, ancho, alto, profundidad):# la clase cubo recibe tres parámetros en el constructor (__init__)
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad

    def calcular_volumen(self):# este metodo multiplica los tres valores
       return self.ancho * self.alto * self.profundidad

# El usuario ingresa los valores por teclado
ancho = float(input("Ingrese el ancho del cubo: "))
alto = float(input("Ingrese el alto del cubo: "))
profundidad = float(input("Ingrese la profundidad del cubo: "))

# Se Crea un objeto cubo con esos valores ingresados y se calcula el volumen
cubo = Cubo(ancho, alto, profundidad)

# Mostrar resultado
print(f"El volumen del cubo es: {cubo.calcular_volumen()}")