# 6.8 Funciones: Valores por Default en Argumentos

def sumar(a = 0, b = 0): # valores por default
    return a + b

resultado = sumar() # si no pasamos argumentos, usa los valores por default
print("El resultado de la suma es:", resultado)  # mostramos el resultado

#le pasamos un solo argumento, el otro usa el valor por default
print("El resultado de la suma es:", {sumar(5, 6)})
