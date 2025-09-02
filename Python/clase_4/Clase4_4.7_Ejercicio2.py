# Ejercicio 2: Modificar los elementos de una lista
# Llenar una lista con los números del 1 al 10, luego modificar los
# elementos de la lista multiplicándolos por un valor ingresado por el usuario.

lista = list(range(1, 11))
print("Lista:", lista)

#ingreso de un numero por el usuario
multiplicador = int(input("Ingrese un número para multiplicar los elementos: "))
lista = [x * multiplicador for x in lista]

print("Lista modificada:", lista)
