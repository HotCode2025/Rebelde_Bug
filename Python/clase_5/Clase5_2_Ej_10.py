# Ejercicio 10: No repetir caracteres
# Hacer un programa que pida una cadena por teclado,
# luego meter los caracteres en una lista sin repetir caracteres.

cadena = input("Ingrese una cadena: ")
lista_sin_repetidos = []

for caracter in cadena:
    if caracter not in lista_sin_repetidos:
        lista_sin_repetidos.append(caracter)

print("Cadena ingresada:", cadena)
print("Lista sin caracteres repetidos:", lista_sin_repetidos)
