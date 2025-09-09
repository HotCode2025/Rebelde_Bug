#Ejercicio 2: Función con * args para multiplicar
#Crear una función para multiplicar los valores recibidos
#de tipo numérico, utilizando argumentos variables *args
#como parámetro de la función y regresar como resultado
# la multiplicación de todos los valores pasados como argumento.

def multiplicar(*args):#Definimos la función multiplicar que acepta una cantidad variable de argumentos posicionales gracias a *args
    """
    Multiplica todos los argumentos numéricos recibidos y devuelve el producto
    Si no se pasan argumentos, devuelve 1 (identidad multiplicativa)
    Da mje de error si algún argumento no es numérico
    """
    resultado = 1 # inicializamos con 1 (identidad multiplicativa: matemáticamente el producto de una lista vacía se define como 1)
    for idx, valor in enumerate(args, start=1):#Recorremos cada argumento recibido
        if not isinstance(valor, (int, float)):  # verificar si no es número
            print(f"El argumento #{idx} ({valor}) no es numérico, por favor utilizar números")#Mje de error, sólo números
            return None  # salta este valor y sigue con el siguiente
        resultado *= valor # multiplicamos acumulando en 'resultado'
    return resultado

print(multiplicar(2, 3, 4))
print(multiplicar(5))
print(multiplicar()) # 1  (convención: producto vacío = 1)
print(multiplicar(2, 0, 5))
print(multiplicar(2.5, 4))
print(multiplicar(2.5, "a"))
print(multiplicar(20, 1, 5))





