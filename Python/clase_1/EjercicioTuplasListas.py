#Dada la siguiente tupla: tupla=(13,1,8,3,2,5,8) Definimos la tupla
#Crear una lista que sólo incluya los números menores a 5 e imprima por consola 1, 3, 2
# Definimos la tupla
tupla = (13, 1, 8, 3, 2, 5, 8)

# Creamos lista vacía
lista_menores_5 = []

# Recorremos la tupla
for numero in tupla:
    if numero < 5:
        lista_menores_5.append(numero)

# Imprimimos resultado
print(lista_menores_5)
