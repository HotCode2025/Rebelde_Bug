# Crear una función para sumar los valores recibidos de tipo numéricos
# utilizando argumentos variables *args como parametro de la funcion 
# y agregar como resultado la suma de todos los valores pasados como argumentos.
def sumarNumeros(*numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    print("La suma es:", suma)

# Ejemplo para ver funcionamiento de código
sumarNumeros(4, 1, 7, 9)
sumarNumeros(11, 23, 6, 8, 4)

