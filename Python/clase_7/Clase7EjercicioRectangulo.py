# Ejercicio Rectángulo
# Crear una clase llamada Rectangulo, debe tener dos atributos: altura y base
# el nombre del metodo será calcular_area utilizando la fórmula:
# area = base * altura. Pero la base y la altura deben ser ingresadas por
# el usuario y los objetos deben ser tres.

class Rectangulo:# clase
    def __init__(self, base, altura):# el constructor __init__ recibe base y altura
        self.base = base # Guarda esos valores en atributos de la instancia(self.base, self.altura)
        self.altura = altura

    def calcular_area(self):# Método multiplica base x altura
        return self.base * self.altura

# Crear tres rectángulos con valores ingresados por el usuario
for i in range(1, 4):# el ciclo se repite tres veces porque pide tres objetos
    print(f"\nRectángulo {i}")
    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura: "))
    rectangulo = Rectangulo(base, altura)# cada vez que pide base y altura al usuario se crea un objeto rectángulo
    print(f"El área del rectángulo {i} es: {rectangulo.calcular_area()}")# Calcula y muestra el área correspondiente