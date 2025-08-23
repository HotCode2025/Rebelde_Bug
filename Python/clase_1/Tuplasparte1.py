# Es similar en muchas cosas a las litas
# Sigue el orden en los elementos que se agregan
# pero éstos no se pueden modificar a esto se lo llama
# INMUTABLE esa es la gran diferencia
# Con las listas podemos usar las funciones append, insert, remove

# Definimos una tupla, no se usan [] sino ()
cocina = ("cuchara", "cuchillo", "tenedor")
print(cocina)
print(len(cocina))# para saber la cant de elementos que  tn la tupla

# Acceder a un elemento, para eso usamos corchetes []
print(cocina[0])
# Mostrar de manera inversa
print(cocina[-1]) # Acá muestra el último elemento
# si quiesiéramos el penúltimo ponemos print(cocina[-2])

# Acceder a un rango
print(cocina[0:1]) # Cdo ponemos un n° tenemeos que saber que va a poner uno menos
# Nos va a mostrar el primer elemento es como si pusiéramos cocina[0] en cto al resultado es lo mismo
print(cocina[0:2])
# Ejemplo
verduras = ("papa") # Esto no es una tupla, es una cadena, un string
verduras = ("papa",) # Cuando le ponemos la coma aunque sea un sólo elemnto es una TUPLA