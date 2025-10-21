#Tarea que el usuario ingrese el número para calcular el factorial

def factorial(numero):
    if numero == 1 or numero == 0:  # caso base (0! = 1 también)
        return 1
    else:
        return numero * factorial(numero - 1)  # caso recursivo

# Pedimos el número al usuario
numero = int(input("Ingrese un número para calcular su factorial: "))

# Llamamos a la función
resultado = factorial(numero)

# Mostramos el resultado
print(f"El factorial del número {numero} es: {resultado}")
