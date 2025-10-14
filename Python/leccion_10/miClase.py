# 13.6 Diagrama de clases UML con variables de clase: Teoría en carpeta Lección10
# 13.7 Variables de clase: Practica en carpeta Lección10
# 14.1 Creación de variables de clase
# 14.2 Métodos estáticos
# 14.3 Métodos de clase
# 14.4 Contexto estático y Dinámico




class MiClase:
    variable_clase = "Valor de la variable de clase"

    def __init__(self, valor_instancia):
        self.variable_instancia = valor_instancia
    
    @staticmethod
    def metodo_estatico():
        print("Este es un método estático")
        print(MiClase.variable_clase)  # Acceso a la variable de clase dentro del método estático
    
    @classmethod
    def metodo_clase(cls): # cls es una convención para referirse a la clase
        print("Este es un método de clase")
        print(cls.variable_clase)  # Acceso a la variable de clase dentro del método de clase
    
    def metodo_instancia(self):
        print("Este es un método de instancia")
        print(self.variable_instancia)  # Acceso a la variable de instancia
        print(MiClase.variable_clase)  # Acceso a la variable de clase


print(MiClase.variable_clase)  # Acceso a la variable de clase

miClase1 = MiClase("Valor de la variable de instancia 1")
print(miClase1.variable_instancia)  # Acceso a la variable de instancia
print(miClase1.variable_clase)  # Acceso a la variable de clase

# cada objeto tiene su propia copia de las variables de instancia nunca comparten
miClase2 = MiClase("Valor de la variable de instancia 2")
print(miClase2.variable_instancia)  # Acceso a la variable de instancia
print(miClase2.variable_clase)  # Acceso a la variable de clase

# crear una nueva variable de clase
MiClase.nueva_variable_clase = "Nueva variable de clase"
print(MiClase.nueva_variable_clase)
print(miClase1.nueva_variable_clase)
print(miClase2.nueva_variable_clase)

MiClase.metodo_estatico ()  # Llamada al método estático
MiClase.metodo_clase ()  # Llamada al método de clase

miibjeto = MiClase("Valor de la variable de instancia 3")
miibjeto.metodo_clase()  # Llamada al método de clase desde un objeto
