#Diccionario compuesto por dos elementos: una llave y un valor
#dict(key,value)
diccionario = {
    'IDE': 'Integrated Development Environment',
    'POO': 'Pogramacion Orientada a Objetos',
    'SABD': 'Sistema de Administracion de Base de Datos'
}

#Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

#Acceder a una parte del diccionario con la llave (key)
print(diccionario['IDE'])

#Otra forma de llamar elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

#Modificacion de elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

#Como recorrer los elementos
#Solo muestra las llaves
for termino in diccionario:
    print(termino)

'''for termino, valor in diccionario:
    print(termino, valor)
DA ERROR POR SER DEMASIADOS VALORES'''

#Necesitamos una funcion para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

#Otras maneras de acceder a un diccionario
for termino in diccionario.keys(): #Usando funcion
    print(termino) #muestra solo las llaves

for valor in diccionario.values(): #usamos una funcion nuevamente
    print(valor)

#Comoprobar existencia de algun elemento
print('IDE' in diccionario) #devuelve un booleano

#Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

#Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

#Vaciar un diccionario
diccionario.clear()
print(diccionario)

#Eliminar diccionario
del diccionario #si se manda a imprimir da error, porque ya se ha eliminado