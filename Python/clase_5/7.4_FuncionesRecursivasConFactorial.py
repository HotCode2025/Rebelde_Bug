#Funciones recursivas

def factorial(numero):
    if numero == 1: # Caso base
        return 1
    else:
        return numero * factorial(numero-1) #Caso recursivo

resultado = factorial(5) #Lo hacemos en codigo duro
print(f'El factorial del número 5 es: {resultado}')

