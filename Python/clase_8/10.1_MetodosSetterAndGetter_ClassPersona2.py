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

Persona1 = Persona2('Ariel', 'Betancud', '42')
print(Persona1.nombre) #Llamamos al método getter

# Tarea método set y get con apellido y edAD

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