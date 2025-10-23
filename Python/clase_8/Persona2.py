class Persona2:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalles(self):
            print(f'Los datos a mostrar son los siguientes: {self.nombre} {self.apellido} {self.edad}')

    @property #decorador
    def nombre(self): #Método Getter
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):        #Método setter
        print('Estamos utilizando el método setter')
        self._nombre = nombre

persona1 = Persona2('Ariel', 'Betancud', '42')
print(persona1.nombre) #Llamamos al método getter

# Tarea método set y get con apellido y edad

@property
def apellido(self):
    return self._apellido


@apellido.setter
def apellido(self, apellido):
    print('Estamos utilizando el método SETTER de apellido')
    self._apellido = apellido

@property
def edad(self):
    return self._edad

@edad.setter
def edad(self, edad):
    print('Estamos utilizando el método SETTER de edad')
    self._edad = edad
persona1.nombre = 'Juan Pedro' #Llamamos el metodo setter
print(persona1.nombre) # metodo getter
print(persona1.mostrar_detalles()) #Llamamos al metodo mostrar detalles

def __del__(self):
    print(f'Persona2: {self._nombre} {self._apeliido}{self._edad}')

#Tarea
# Creación de 4 objetos nuevos
persona1 = Persona2("Melina", "Gallo", 30)
persona2 = Persona2("Carlos", "Lopez", 28)
persona3 = Persona2("Julieta", "Fernandez", 35)
persona4 = Persona2("Mateo", "Sanchez", 22)

# Mostrar detalles de cada objeto
print("Detalles de las personas creadas")
persona1.mostrar_detalles()
persona2.mostrar_detalles()
persona3.mostrar_detalles()
persona4.mostrar_detalles()

# Modificar algunos datos con los setters
print("Modificando algunos datos")
persona1.nombre = "Melina Denise"
persona2.edad = 29
persona3.apellido = "Fernandez Vega"
persona4.nombre = "Mateo Ariel"

# Mostrar detalles nuevamente
print("Detalles actualizados")
persona1.mostrar_detalles()
persona2.mostrar_detalles()
persona3.mostrar_detalles()
persona4.mostrar_detalles()

print(__name__)