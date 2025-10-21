class Persona: # Creamos una clase
    def __init__(self, nombre, apellido, edad): #Se lo llama metodo init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

persona1 = Persona('Melina', 'Denise', 37) #Necesitamos enviar argumentos
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona('Osvaldo', 'Giordanini', 45)
#print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} {persona2.edad}')

#Tarea, realizar el print:

print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} {persona1.edad}')
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} {persona2.edad}')

