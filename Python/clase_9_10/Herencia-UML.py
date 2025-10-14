class Animal:
    def __init__(self, especie, nombre, edad):
        self.__especie = especie
        self.__nombre = nombre
        self.__edad = edad

    @property
    def especie(self):
        return self.__especie

    @especie.setter
    def especie(self, nueva_especie):
        self.__especie = nueva_especie

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad

    def __str__(self):
        return f"Animal: {self.__nombre}, Especie: {self.__especie}, Edad: {self.__edad}"


class Persona:
    def __init__(self, nombre, estatura, edad, mascota: Animal = None):
        self.__nombre = nombre
        self.__estatura = estatura
        self.__edad = edad
        self.__mascota = mascota  # relación con Animal

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def estatura(self):
        return self.__estatura

    @estatura.setter
    def estatura(self, nueva_estatura):
        if nueva_estatura > 0:
            self.__estatura = nueva_estatura

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad

    @property
    def mascota(self):
        return self.__mascota

    @mascota.setter
    def mascota(self, nueva_mascota: Animal):
        self.__mascota = nueva_mascota

    def __str__(self):
        if self.__mascota:
            return f"Persona: {self.__nombre}, Edad: {self.__edad}, Estatura: {self.__estatura} m, Mascota: ({self.__mascota})"
        else:
            return f"Persona: {self.__nombre}, Edad: {self.__edad}, Estatura: {self.__estatura} m, sin mascota"


#Ejemplo de uso:
animal1 = Animal("Gato", "Mushu", 2)
persona1 = Persona("Jimena", 1.58, 24, animal1)
print(persona1)