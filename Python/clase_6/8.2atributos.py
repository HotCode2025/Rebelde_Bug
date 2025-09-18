# 8.2 Atributos en métodos y creación de un objeto

class Persona:
    def __init__(selfd): # El método __init__ es el constructor de la clase:  llamado init duder
        selfd.nombre = "Ruben"
        selfd.apellido = "Gonzalez"
        selfd.edad = 30

Persona1 = Persona() # Creación de un objeto de la clase Persona

print(Persona1.nombre)
print(Persona1.apellido)
print(Persona1.edad)
print(Persona)