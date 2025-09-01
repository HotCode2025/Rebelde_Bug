# Inicializamos la variable suma en 0
suma = 0

# Recorremos todos los números del 2 al 30
for numero in range(2, 31):  # range(2, 31) va desde 2 hasta 30 inclusive
    # Verificamos si el número es par
    if numero % 2 == 0:
        suma = suma + numero  # Sumamos el número a la variable suma

# Mostramos el resultado
print("La suma de los números pares del 2 al 30 es:", suma)

