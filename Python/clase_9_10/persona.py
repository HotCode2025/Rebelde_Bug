class Persona: # Esta clase hereda de la clase Object
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    

@property
def nombre(self):
    return self._nombre

@nombre.setter
def nombre(self, nombre):
    self._nombre = nombre

@property
def edad(self):
    return self._edad

@edad.setter
def edad(self, edad):
    self.edad = edad

def __str__(self): # Override = sobreescribir
    return f"Persona: [ Nombre: {self._nombre}, Edad: {self._edad} ]"

class Empleado(Persona): # Esta clase es hija de la clase Persona
    def __init__(self,nombre,edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
    
@property
def sueldo(self):
    return self._sueldo

@sueldo.setter
def sueldo(self, sueldo):
    self._sueldo = sueldo

def __str__(self):
    return f'Empleado: [ Sueldo: {self._sueldo} ] {super().__str__()}'

emplado1 = Empleado('maxi',28,75000)
print(emplado1.nombre)
print(emplado1.edad)
print(emplado1.sueldo)