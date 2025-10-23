class Persona2:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self.nombre} {self.apellido} {self.edad}')

    @property  # decorador getter
    def nombre(self):
        return self._nombre

    @nombre.setter  # setter de nombre
    def nombre(self, nombre):
        print('Estamos utilizando el método SETTER de nombre')
        self._nombre = nombre

    @property  # getter de apellido
    def apellido(self):
        return self._apellido

    @apellido.setter  # setter de apellido
    def apellido(self, apellido):
        print('Estamos utilizando el método SETTER de apellido')
        self._apellido = apellido

    @property  # getter de edad
    def edad(self):
        return self._edad

    @edad.setter  # setter de edad
    def edad(self, edad):
        print('Estamos utilizando el método SETTER de edad')
        self._edad = edad


# Solo se ejecutará si este archivo se ejecuta directamente (no cuando se importe)
if __name__ == '__main__':
    # Tarea: creación de 4 objetos nuevos
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

    print("Nombre del módulo:", __name__)
