# Se hace de nuevo la Clase Persona por motivos de muestra más clara y limpia del ejercicio
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre   # atributo privado 1
        self.__edad = edad       # atributo privado 2

    # Getter y Setter para nombre
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    # Getter y Setter para edad
    def get_edad(self):
        return self.__edad

    def set_edad(self, nueva_edad):
        self.__edad = nueva_edad

    # Método mostrar_detalles

    def mostrar_detalles(self):
        print(f"Nombre: {self.__nombre}, Edad: {self.__edad}")


# Creación de los 3 objetos 
persona1 = Persona("Ana", 20)
persona2 = Persona("Luis", 25)
persona3 = Persona("María", 30)

# Muestra de los detalles iniciales
print("Detalles iniciales:")
persona1.mostrar_detalles()
persona2.mostrar_detalles()
persona3.mostrar_detalles()

# Uso de los setters para modificar los datos
persona1.set_nombre("Ana Paula")
persona1.set_edad(21)

persona2.set_nombre("Luis Alberto")
persona2.set_edad(26)

persona3.set_nombre("María José")
persona3.set_edad(31)

# Se muestran los cambios
print("\nDetalles después de modificar:")
persona1.mostrar_detalles()
persona2.mostrar_detalles()
persona3.mostrar_detalles()
