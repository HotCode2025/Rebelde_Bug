# Ejercicio 9: Mostrar una frase sin espacios y contar su longitud
# Hacer un programa donde el usuario ingrese una frase, se le
# devolverá la misma frase pero sin espacios en blanco, y
# además un contador de cuántos caracteres tiene la frase
# (sin contar los espacios en blanco)
# Ejemplo:   frase = vivir por siempre en paz
#            frase final = vivirporsiempreenpaz
#            Nº de caracteres = 20


# 1. Pedir al usuario una frase
frase = input("Ingrese una frase: ")

# 2. Eliminar los espacios en blanco usando replace()
#    - replace(" ", "") reemplaza cada espacio por nada.
frase_sin_espacios = frase.replace(" ", "")

# 3. Calcular la cantidad de caracteres de la frase sin espacios
longitud = len(frase_sin_espacios)

# 4. Mostrar los resultados
print("\nFrase original: ", frase)
print("Frase sin espacios: ", frase_sin_espacios)
print("Número de caracteres (sin contar espacios):", longitud)