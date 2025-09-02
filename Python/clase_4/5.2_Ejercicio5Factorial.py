#Ejercicio 5: Hacer un programa para calcular el factorial de un numero positivo

numero = int(input("Ingrese un número positivo: "))

if numero < 0:
    print("No existe el factorial de un número negativo.")
else:
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    
    print(f"El factorial de {numero} es: {factorial}")