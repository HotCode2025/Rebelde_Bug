class Persona: # Creamos una clase
    def __init__(self, nombre, apellido, edad): #Se lo llama metodo init Dunder
        self.nombre = 'Juan'
        self.apellido = 'Zalazar'
        self.edad = '22'

persona1 = Persona('Melina', 'Denise', 37) #Necesitamos enviar argumentos
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)