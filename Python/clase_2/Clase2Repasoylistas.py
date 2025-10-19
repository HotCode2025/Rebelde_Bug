# LISTAS
# Son colecciones en Python
# Las LISTAS en otros lenguajes se conocen como ARREGLOS O VECTORES
# lista = Ariel, Liliana, Natalia, Osvaldo

nombres = ["Naty", "Osvaldo","Lily","Ariel"]
print(nombres)
print(nombres[0:2])#solo muestra el indice 0, 1 pero no el indice 2
#ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ :3])#indices a mostrar 0,1,2
# Desde el indice indicado hasta el final
print(nombres[1: ])#desde el indice 1 hsta el final
# Modificamos un valor
nombres[2] = "Liliana"
nombres[0]="Natalia"
print(nombres)
for nombre in nombres: # nombre es singular, la lista es plural
    print(nombre)
else:
    print("Se acabaron los elementos de la lista")

# Preguntamos cuantos elementos tiene
print(len(nombres)) # le pasamos como parametro la lista

# Agregamos un elememto
nombres.append("Marcelo")
nombres.append([1,2,3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4,5])
nombres.append(7)
# Una lista puede tener diferentes tipos de datos
print(nombres)
print(len(nombres))
# Insertar un elemento en un indice especifico
nombres.insert(1,"Alberto")
print(nombres)
nombres.insert(3, "Debora")
print(nombres)

# Eliminamos un elemento
nombres.remove("Alberto")
print(nombres)

# Eliminamos el último elemento
nombres.pop()# por default borra el último elemeto de la lista
print(nombres)

# Eliminar u nindice especifico
del nombres[2]# del significa delete (eliminar)
print(nombres)

# Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

# Eliminar la lista
#del nombres
#print(nombres)# Esto da un error dice que nombres no está definido
# es decir que lo ha borrado, en normal que muestre ese error al borrar
print(len(nombres))
