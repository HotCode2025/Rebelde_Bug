# Ejercicio 3: Insertar elementos y ordenarlos
# Pedir números y meterlos en una lista, cuando el usuario
# introduzca un número 0, nuestro programa dejaría de insertar.
# Por último, mostrar los números ordenados de menor a mayor

# 1. Crear lista vacía
numeros = []

print("Ingrese números (para terminar escriba 0):")

# 2. Pedir números en un bucle
while True:
    num = int(input("Número: "))
    if num == 0:  # condición de salida
        break
    numeros.append(num)  # agregar número a la lista

# 3. Ordenar la lista de menor a mayor
numeros.sort()

# 4. Mostrar el resultado
print("Números ordenados de menor a mayor:", numeros)