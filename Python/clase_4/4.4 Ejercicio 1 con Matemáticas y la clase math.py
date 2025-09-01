# Importamos la librería math para usar la función sqrt
import math

# Pedimos al usuario que ingrese un número positivo
numero = float(input("Ingrese un número positivo: "))

# Verificamos que el número sea positivo usando while
while numero < 0:
    print("El número debe ser positivo. Intente de nuevo.")
    numero = float(input("Ingrese un número positivo: "))

# Calculamos la raíz cuadrada usando math.sqrt
raiz = math.sqrt(numero)

# Mostramos el resultado
print("La raíz cuadrada de", numero, "es:", raiz)