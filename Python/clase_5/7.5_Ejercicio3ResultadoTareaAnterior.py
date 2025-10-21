#Ejercicio 3
# Ejercicio 3: Función Recursiva
# Imprimir números de manera descendente usando funciones recursivas.
# Si el usuario ingresa un número negativo, no imprime nada.

def imprimir_descendente(n):
    if n <= 0:  # caso base o si el número es negativo
        return
    else:
        print(n)
        imprimir_descendente(n - 1)  # llamada recursiva

# Solicitamos el número al usuario con validación
try:
    numero = int(input("Ingrese un número positivo: "))

    if numero > 0:
        imprimir_descendente(numero)
    elif numero == 0:
        print("El número es 0, no hay nada que imprimir.")
    else:
        print("No se imprimen números negativos.")

except ValueError:
    print("Error: Debe ingresar un número entero válido.")
