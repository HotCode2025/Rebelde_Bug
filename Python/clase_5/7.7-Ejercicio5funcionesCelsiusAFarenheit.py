# Ejercicio 5: Conversor de temperaturas

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("--- Conversor de Temperaturas ---")
print("1. Celsius a Fahrenheit")
print("2. Fahrenheit a Celsius")

opcion = input("Elegí una opción: ")

if opcion == "1":
    celsius = float(input("Ingresá la temperatura en Celsius: "))
    print("Equivale a:", celsius_a_fahrenheit(celsius), "°F")
elif opcion == "2":
    fahrenheit = float(input("Ingresá la temperatura en Fahrenheit: "))
    print("Equivale a:", fahrenheit_a_celsius(fahrenheit), "°C")
else:
    print("Opción no válida.")