from Clase12_Vid16_2_ClaseEmpleado import Empleado
from Clase12_Vid16_3_ClaseGerente import Gerente


def imprimir_detalles(objeto):
    # print(objeto)  # de manera indirecta llama al str de la clase empleado
    print(type(objeto))  # esto es para saber el tipo de dato que recibe
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente):  # lineas agregadas en video 6
        print(objeto.departamento)  # lineas agregadas en video 6


empleado = Empleado('Jimena', 50000)
imprimir_detalles(empleado)

gerente = Gerente('Adriana', 60000, 'Sistemas')
imprimir_detalles(gerente)
