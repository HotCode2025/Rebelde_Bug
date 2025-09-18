# 6.9 Funciones: Argumentos, Variables en Funciones

# variables en funciones

def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)

listarNombres("juan", "pedro", "maria", "ana")
listarNombres("carlos", "luis")
