# "Maradona":10 Un diccionario esta compuesto por dos elementos
# Una llave y un valor
# dict(key.value)
diccionario = {
    "IDE":"Integrated Development Environment",
    "POO":"Programación Orientada a Objetos",
    "SABD":"Sistema de Administración de Base de Datos"
}
# verificar la cantidad de elemtos del diccionario
print(len(diccionario))
print(diccionario)
# Ctrl + Z vuelve atrás por si tenemos un error, es como el deshacer
# Un diccionario se parece a un tipo SET porque no tenemos índice
# Para acceder lo hacemos desde la llave o key

# Acceder a un diccionario con la llave (key)
print(diccionario["IDE"])# nos muestra el valor asociado a esa llave "IDE" RESPETAR MAYUSCULAS Y ACENTO
print(diccionario.get("POO"))# Aquí usamos la función .get es otra manera de acceder al elemento de un diccionario
print(diccionario.get("SABD"))

# Modificamos elementos
diccionario["IDE"] = "Entorno de Desarrollo Integrado"# un diccionario puede modificarse
print(diccionario)

# Como recorrer elementos
for termino in diccionario:# recorremos mostrando sólo las llavaes
    print(termino)
# Necesitamos una función para recorrer un diccionario
for termino, valor in diccionario.items(): # usamos la función .items, no olvidar los dos puntos al final de la línea del for
    print(termino, valor)
# Otras maneras de acceder a un diccionario
for termino in diccionario.keys():# Estamos usando la función .keys
    print(termino)# muestra sólo las llaves

for valor in diccionario.values():# Usamos la funcion .values para acceder al valor
    print(valor)

# Comprobar la existencia de algún elemento
print("IDE" in diccionario)# devuelve un valor booleano

# Agregar un elemento
diccionario["PK"] = "Primary key"
print(diccionario)
# CUIDADO! SI AGREGAMOS CON UNA LLAVE EXISTENTEE SOBREESCRIBE CON EL NUEVO VALOR

# Eliminar un elemento
diccionario.pop("SABD")# función .pop para eliminar
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)# aparecen las llaves vacías

# Eliminar diccionario
#del diccionario # el diccionario se borró
print(diccionario)

# Concatenamos listas
lista1 = [1,2,3,1]
lista2 = [4,5,6,1]
lista3 = lista1+lista2# Concatenación
print(lista3)

lista3.extend([7,8,9,1])# función para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5))# Esta función .index es para saber en que índice está el elemento o valor ingresado
# print(lista3.index(0)) # esto da error porque el elmento no está en la lista

# Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1)) # Cuenta cuantos valores iguales hay dentro de la lista

# Para poner una lista al revés
lista3.reverse()
print(lista3)