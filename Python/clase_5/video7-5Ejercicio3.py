def cuenta_regresiva(n):
    # Caso base: si n es menor o igual a 0, no imprime nada
    if n <= 0:
        return
    
    # Imprimir el número actual
    print(n, end="")
    
    # Agregar coma y espacio si no es el último número (1)
    if n > 1:
        print(", ", end="")
    
    # Llamada recursiva con n-1
    cuenta_regresiva(n - 1)

# Pedir al usuario que ingrese un número
numero = int(input("Ingresa un número positivo: "))

# Llamar a la función recursiva
cuenta_regresiva(numero)