# Clase 4 Ejercicios y Más -> Tarea

# 4.1  Ejercicio de Colecciones 1

# Ejercicio 1 - Eliminar duplicados de una lista

# Escriba un programa donde tenga una lista y que, a 
# continuación, elimine los elementos repetidos. Por 
# último, mostrar la lista

# Se crea la lista
clases_wow = ["paladin", "cazador", "paladin", "evocador", "cazador", "druida"]

# Lista vacía para guardar los elementos sin repetir
clases_sin_duplicados = []

# Recorrer cada elemento de la primera lista
for elemento in clases_wow:
    # Si el elemento no está en la nueva lista, se agrega a la segunda lista vacía
    if elemento not in clases_sin_duplicados:
        clases_sin_duplicados.append(elemento)

# Se muestran las listas
print(f"Lista original: {clases_wow}")
print(f"Sin duplicados: {clases_sin_duplicados}")

