#Pilas usando Listas
pila = [1, 2, 3]

#Agregar elementos a la pila por el final
pila.append(6)
pila.append(9)
print(pila)

#Sacamos elementos a la pila desde el final
elementoBorrado = pila.pop() # Quita el último elemento y lo guarda en la variable 
print(f'Sacamos el elemento {elementoBorrado}')
print(f'La pila ahora quedó así: {pila}')