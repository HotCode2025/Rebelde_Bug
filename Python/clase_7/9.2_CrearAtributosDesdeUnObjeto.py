class Persona: # Creamos una clase
    def __init__(self, nombre, apellido, edad): #Se lo llama metodo init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def mostrar_detalle(self):
        print({f'Persona: {self.nombre} {self.apellido} {self.edad}'})


persona1 = Persona('Melina', 'Denise', 37) #Necesitamos enviar argumentos
#print(persona1.nombre)
#print(persona1.apellido)
#print(persona1.edad)

persona2 = Persona('Osvaldo', 'Giordanini', 45)
#print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} {persona2.edad}')

#Tarea, realizar el print:

print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} {persona1.edad}')
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} {persona2.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
persona1.edad ='40'
print(f'El objeto2 de la clase persona: {persona1.nombre} {persona1.apellido} {persona1.edad}')

#Los atributos son caracteristicas
#Los métodos son el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle()
persona2.mostrar_detalle()

#Persona.mostrar_detalle(persona1) #Debemos pasarle una referencia para el self o nos dará error
persona1.telefono = '0303456'
print(f'Este es el teléfono:{persona1.telefono}') #Hemos creado un atributo de un objeto
#print(persona1.telefono) El objeto persona2 no tiene atributo