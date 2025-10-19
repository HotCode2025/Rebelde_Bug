# Definimos una tupla, no se usan [] sino ()
cocina = ("cuchara", "cuchillo", "tenedor")
print(cocina)
print(len(cocina))# para saber la cant de elementos que  tn la tupla

# Acceder a un elemento, para eso usamos corchetes []
print(cocina[0])
# Mostrar de manera inversa
print(cocina[-1]) # Acá muestra el último elemento
# Acceder a un rango
print(cocina[0:1]) # Cdo ponemos un n° tenemos que saber que va a poner uno menos
print(cocina[0:2])

# Recorremos los elementos de la tupla
for cocinar in cocina:
   # print(cocinar) # print está usando \n para saltos de líneas
    print(cocinar, end= " ") # para cambiar esto ponemos coma y end
   # usamos end= para eliminar los saltos de línea
# No se puede modificar una tupla
# cocina[0] = "platos"
# print(cocina) ESTO DA ERROR

# Como modificar una tupla, no ese recomendable, sólo si es estrictamente necesario
# Se hace una conversión de tupla a lista y luego de lista a tupla
cocinaLista = list(cocina)
cocinaLista[0] = "plato"
cocina = tuple(cocinaLista)
print("\n",cocina)

# del cocin: esto es para eliminar una tupla