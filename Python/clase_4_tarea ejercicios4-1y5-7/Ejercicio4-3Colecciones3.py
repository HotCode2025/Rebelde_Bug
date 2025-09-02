# Ejercicio 3: Agregar personajes a una lista
# Escriba un programa donde cree una lista con los siguientes
# personajes del señor de los anillos

# Nombre: Aragon
# Clase: Guerrero
# Raza: Dúnadan del norte
# Nombre: Gandalf
# Clase: Mago
# Raza: Istar
# Nombre: Legolas
# Clase: Arquero
# Raza: Elfo Síndar

# Creamos una lista de diccionarios, donde cada diccionario representa un personaje
personajes = [
    {"Nombre": "Aragon", "Clase": "Guerrero", "Raza": "Dúnadan del norte"},
    {"Nombre": "Gandalf", "Clase": "Mago", "Raza": "Istar"},
    {"Nombre": "Legolas", "Clase": "Arquero", "Raza": "Elfo Síndar"}
]

# Mostramos los personajes
print(f"A continuación se detallan personajes del Señor de los Anillos y sus características:")
for personaje in personajes:
    print(f"Nombre: {personaje['Nombre']}, Clase: {personaje['Clase']}, Raza: {personaje['Raza']}")

