#Ejercicio 4.6: Llenar una lista
#Llenar una lista con los numeros del 1 al 50, luego mostra
#la lista con el bucle for, los elementos deben mostrarse
#de la siguiente forma
#1-2-3-4-5...-50

numeros = list(range(1, 51))
for i in range(len(numeros)):
    if i < len(numeros) - 1:
        print(numeros[i], end="-")
    else:
        print(numeros[i])