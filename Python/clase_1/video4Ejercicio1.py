#Ejercicio 1
#Iterar un rango de 0 a 10 e imprimir números divisibles entre 3
print("-" * 30) #Print con división 

for i in range(0, 10): #ciclo for que recorre un rango de 0 a 10
    if i % 3 == 0:     #condicional que imprime el contador (i)
        print(i)       # si éste módulo 3 es igual a 0

print("-" * 30)