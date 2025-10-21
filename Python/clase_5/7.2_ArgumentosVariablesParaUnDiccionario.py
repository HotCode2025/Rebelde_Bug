# Argumentos variables en funciones
def listarNombres(*nombres): #Normalmente se utiliza *args
    for nombre in nombres: #Se va a convertir en una tupla
        print(nombre)
listarNombres('Liva', 'Zoe', 'Jime', 'Cami', 'José', 'Maxi', 'Meli', 'Mica', 'Rubén')
listarNombres('Ariel', 'Osvaldo', 'Nati', 'Pepe', 'Nico', 'Mati', 'Marcela', 'Carlos')

def listarTerminos(**terminos): # Lo mas utilizado es *kwargs para recibir los argumentos
    for llave, valor in terminos.items(): #kwargs significa key words arguments
        print(f'{llave}:{valor}')

listarTerminos()
listarTerminos(IDE='Integrated Development Enviroment', PK='Primary Key')
listarTerminos(Nombre='Leonel Messi')