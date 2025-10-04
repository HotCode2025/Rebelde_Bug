# 9.1 Palabra reservada self y atributos de instancia
# 9.2 Crear atributos desde un objeto
# 9.7 Método init Dunder con argumentos variables
# 9.8 Encapsulamiento Parte 1


class Persona:
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs): # args y kwargs son opcionales
        self.__nombre = nombre # Atributo privado no se puede acceder desde fuera de la clase
        self.apellido = apellido
        self.edad = edad
        self.args = args
        self.kwargs = kwargs
    def mostrar_detalle(self):
        print(f"la clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self.edad}, la direccion es {self.args}, los datos importantes son {self.kwargs}")
        
Persona1 = Persona("Ruben", "Gonzalez", 30)
# Persona.mostrar_detalle(Persona) Debemos pasarle una refetencia para el self o da error


Persona1.cel = "6556542366"
persona2 = Persona("Juan", "Perez", 3589236, 25, "Calle Falsa 123", "Piso 1", "Departamento A", tel="123456789", email="perex32@gmail.com")
print(Persona1.cel)
persona2.mostrar_detalle()

# print(persona3._dni) # No da error pero no es recomendable acceder a atributos protegidos
# print(persona2.__nombre) # Da error porque el atributo es privado