# Ejercicio 6: Tabla de multiplicar
# Hacer un programa que pida un número por teclado y guarde
# en una lista su tabla de multiplicar hasta el 10. Por ejemplo:
# Si digita el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50

# Pedir un número al usuario
# La función input() recibe el dato como texto, por eso usamos int()

num = int(input("Ingrese un número: "))

# Crear una lista con la tabla de multiplicar

tabla = []

# Recorremos los números del 1 al 10 con un bucle for.
# En cada repetición multiplicamos el número ingresado (num)
# por el valor de i (que va de 1 a 10).

for i in range(1, 11):  # range(1, 11) genera los números 1,2,3,...,10
    resultado = num * i     # calculamos el producto
    tabla.append(resultado) # agregamos el resultado a la lista

#  Mostrar la lista resultante
# Usamos f-string para imprimir el número ingresado y su tabla.
print(f"Tabla de multiplicar del {num}:", tabla)