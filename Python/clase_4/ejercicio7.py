# Clase 4 Funciones y Ejercicios -> tarea

# 5.6 Ejercicio 7 - Juego Adivina el Número

# Realizar un juego para adivinar un número. Para ello, se
# debe generar un número aleatorio entre 1 - 100, y luego ir 
# pidiendo números, indicando "es mayor" o "es menor", según
# sea mayor o menos con respecto al número que el usuario 
# ingrese para adivinar. El proceso termina cuando el 
# usuario acierta, y allí se debe mostrar el número de
# intentos. 

# Se importa la librería para generar números aleatorios
import random  

# Generar un número aleatorio
numero_secreto = random.randint(1, 100)

# Contador contador para los intentos
intentos = 0

print("¡Adivina el número secreto entre 1 y 100!")

while True:
    # Se pide al usuario que ingrese un número
    intento = int(input("Ingresa un número: "))
    intentos += 1  # Se suma un intento

    # Comparación con el número secreto
    if intento < numero_secreto:
        print("El número secreto es mayor.")
    elif intento > numero_secreto:
        print("El número secreto es menor.")
    else:
        print("¡Correcto! El número secreto era", numero_secreto)
        print("Número de intentos:", intentos)
        break  # Se sale del bucle cuando se acierta



