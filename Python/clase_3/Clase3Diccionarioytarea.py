# Diccionarios

seleccionArgentina = {
10: {"Nombre": "Lionel Messi", "Edad": 35, "Altura": 1.70, "Precio": "50 millones", "Posicion": "Extremo derecho"},
11: {"Nombre": "Angel Di Maria", "Edad": 34, "Altura": 1.80, "Precio": "12 millones", "Posicion": "Extremo"},
24: {"Nombre": "Paulo Dybala", "Edad": 28, "Altura": 1.77, "Precio": "35 millones", "Posicion": "Media punta"},
19: {"Nombre": "Nicolas Otamendi", "Edad": 34, "Altura": 1.83, "Precio": "3.5 millones", "Posicion": "Defensa central"},
1: {"Nombre": "Franco Armani", "Edad": 35, "Altura": 1.89, "Precio": "3.5 millones", "Posicion": "Portero"},
}
#print(seleccionArgentina)
#print(seleccionArgentina[10])
#print(seleccionArgentina.values())#sólo muestra los valores del diccionario

#for llave in seleccionArgentina:#recorremos el arreglo con el ciclo for
#   print(llave)#acá muestra sólo las llaves, los números de los jugadores

#for llave, valor in seleccionArgentina.items():
#   print(llave, valor)

#Tarea: Agregar al menos 4 jugadores más al diccionario: seleccionArgentina
del seleccionArgentina[11]
del seleccionArgentina[1]
del seleccionArgentina[24]
seleccionArgentina[10] ={"Nombre": "Lionel Messi", "Edad": 38, "Altura": 1.70, "Precio": "18 millones", "Posicion": "Extremo derecho"}
seleccionArgentina[22] = {"Nombre": "Lautaro Martínez", "Edad": 28, "Altura": 1.75, "Precio": "75 millones", "Posicion": "Delantero"}
seleccionArgentina[23] = {"Nombre": "Emiliano Martínez", "Edad": 32, "Altura": 1.96, "Precio": "20 millones", "Posicion": "Arquero"}
seleccionArgentina[9] = {"Nombre": "Julián Álvarez", "Edad": 25, "Altura": 1.70, "Precio": "90 millones", "Posicion": "Delantero"}
seleccionArgentina[13] = {"Nombre": "Cristian Romero", "Edad": 27, "Altura": 1.85, "Precio": "60 millones", "Posicion": "Defensa central"}
seleccionArgentina[5] = {"Nombre": "Leandro Paredes", "Edad": 31, "Altura": 1.80, "Precio": "8 millones", "Posicion": "Mediocampista"}
seleccionArgentina[3] = {"Nombre": "Nicolás Tagliafico", "Edad": 32, "Altura": 1.72, "Precio": "5 millones", "Posicion": "Defensa lateral"}
seleccionArgentina[41] = {"Nombre": "Franco Mastantuono", "Edad": 18, "Altura": 1.77, "Precio": "45 millones", "Posicion": "Mediocampista/Extremo"}
seleccionArgentina[19] = {"Nombre": "Nicolas Otamendi", "Edad": 37, "Altura": 1.83, "Precio": "1 millon", "Posicion": "Defensa central"}

for llave, valor in seleccionArgentina.items():
    print(llave, valor)
print("Tenemos cargados en el diccionario la cantidad de jugadores: ", end= " ")
print(len(seleccionArgentina))


