# Lista = datos que pueden cambiar (mutable).

#lista = 0 pepe, 1 juan, 2 maria, 3 jose, 4 luis
lista = ['pepe', 'juan', 'maria', 'jose', 'luis']
print("TODO",lista)  # Imprime la lista completa
print("EL PRIMERO",lista[0])  # Imprime 'pepe'
print("EL ULTIMO",lista[-1])  # imprime el ultimo elemento de la lista
print("EL PENULTIMO",lista[-2])  # imprime el penultimo elemento de la lista

# Imprime desde el indice 0 hasta el indice 2-1 (no incluye el indice 2
print("SOLO EL PRIMERO Y SEGUNDO",lista[0:2])   

# ir del inicio de la lista al indice (sin incluirlo)
print("DESDE EL INICIO AL INDICADO ",lista[ :3]) 

# desde el indice indicado hasta el final de la lista
print("DESDE EL INDICADO HASTA EL FINAL",lista[2:])

# modificar un elemento de la lista
lista[0] = 'pepe modificado'
print("MODIFICADO", lista)  

# iterar una lista
for nombre in lista:
    print("ITERANDO", nombre)
else :
    print("se ha terminado de iterar la lista")


# preguntar cuantos elementos hay en la lista
print("HAY", len(lista), "ELEMENTOS EN LA LISTA")

# añadir un elemento al final de la lista
lista.append('nuevo')
print("AÑADIDO", lista)

# Añadir un elemento en una posicion concreta
lista.insert(2, 'insertado')
print("INSERTADO 2", lista)
lista.insert(0, 'PEPE')
print("INSERTADO 3", lista)

# eliminar un elemento de la lista
lista.remove('pepe modificado')
print("ELIMINADO 'pepe modificado'", lista)

# Eliminar el ultimo elemento de la lista
lista.pop()
print("ELIMINADO EL ULTIMO", lista)

# Eliminar un elemento de la lista por su indice
del lista[2]
print("ELIMINADO EL ELEMENTO DE INDICE 2", lista)

# Eliminar todos los elementos de la lista
lista.clear()
print("LISTA LIMPIADA", lista)

# ELIMINAR LA LISTA COMPLETA
del lista
print("LISTA ELIMINADA")  # Esto no imprimirá nada porque la lista ya ha sido eliminada