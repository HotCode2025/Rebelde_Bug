# Ejercicio 2: Operaciones de conjuntos con listas
# Escriba un programa que tenga 2 listas y que a continuación
# cree las siguientes listas (en las que no deben haber repetición)
# 1 Lista de palabras que aparecen en las listas
# 2 Lista de palabras que aparecen en la primera lista, pero no en la segunda
# 3 lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4 lista de palabras que aparecen en ambas listas

l1videojuegos = ['Call of duty', 'Resident Evil 4', 'Minecraft', 'The Last of Us', 'Mario Bros']
l2animales = ['Leopardo', 'Carpincho', 'Guanaco', 'Minecraft', 'Anaconda', 'Pejerrey']

# Convertir a conjuntos para operaciones sin repeticiones
set1 = set(l1videojuegos)
set2 = set(l2animales)

# 1. Palabras que aparecen en ambas listas (unión)
print('*** Lista de palabras que aparecen en ambas listas  ***')
print(set1.union(set2))

# 2. Palabras que están en la primera lista pero no en la segunda (diferencia)
print('*** Solo palabras de la primera lista ***')
print(set1.difference(set2))

# 3. Palabras que están en la segunda lista pero no en la primera (diferencia)
print('*** Solo palabras de la segunda lista ***')
print(set2.difference(set1))

# 4. Palabras que están en ambas listas (intersección)
print('*** Palabras que aparecen en ambas listas ***')
print(set1.intersection(set2))