# 14.6 Ejercicio Contador 
# 14.7 Mejoras en el ejercicio Contador
class Persona:
    contador_personas = 0  # variable de clase

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas

    def __init__(self, nombre, edad):
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona[id_persona={self.id_persona}, nombre={self.nombre}, edad={self.edad}]"


# Ejemplo de uso
if __name__ == "__main__":
    persona1 = Persona("Juan", 30)
    print(persona1)
    persona2 = Persona("Ana", 25)
    print(persona2)
    persona3 = Persona("Luis", 40)
    print(persona3)
    print(f"Cantidad de personas: {Persona.contador_personas}")