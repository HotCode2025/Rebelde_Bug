# 9.3 Crear la clase Aritmética: Sumar
# 9.4 Clase Aritmética: Resta, multiplicación y división
class Aritmetica:
    """
    El nombre de este tipo de comentarios es : DocString
    Esto es documentación de la clase en Python.

    Vamos a hacer en esta clase algunas operaciones:
    suma, resta, multiplicación y más.
    """

    # El constructor ahora recibe 2 parámetros
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    # Método para sumar
    def sumar(self):
        return self.operandoA + self.operandoB
    
    def resta(self):
        return self.operandoA - self.operandoB
    
    def multiplicar(self):
        return self.operandoA * self.operandoB
    
    def dividir(self):
        return self.operandoA / self.operandoB


# Crear un objeto de la clase Aritmetica
Aritmetica1 = Aritmetica(7, 9)

# Llamar a los métodos y mostrar resultados
print(f"La suma de los números es: {Aritmetica1.sumar()}")            
print(f"La resta de los números es: {Aritmetica1.resta()}")       
print(f"La multiplicación de los números es: {Aritmetica1.multiplicar()}") 
print(f"La división de los números es: {Aritmetica1.dividir()}")      