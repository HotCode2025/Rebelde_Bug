# 12.1 Herencia Múltiple UML teoría
# 12.2 Creamos las clases padres
# 13.4 Clases abstractas: Diagrama de clases UML, teoría y practica

# ABC = Abstract Base Class convierte una clase en abstracta
from abc import ABC, abstractmethod

class FiguraGeometrica (ABC):
    def __init__(self, ancho, alto):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 1  # Valor por defecto si el ancho no es válido
            print("Ancho no válido, se asigna valor por defecto 1")
        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 1  # Valor por defecto si el alto no es válido
            print("Alto no válido, se asigna valor por defecto 1")
    @property
    def ancho(self):
        return self._ancho
    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print("Ancho no válido, no se modifica el valor")
    @property
    def alto(self):
        return self._alto
    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print("Alto no válido, no se modifica el valor")
    def __str__(self):
        return f"Ancho: {self.ancho}, Alto: {self.alto}"
    
    @abstractmethod
    def calcular_area(self):
        pass
    # metodo encamsulado
    def _validar_valor(self, valor):
        return True if 0 < valor < 20 else False

    