from mundo_pc.Clase17_4_Vid4_ClaseHijaRaton import Raton
from mundo_pc.Clase17_5_Vid5_ClaseHijaTeclado import Teclado
from mundo_pc.Clase17_6_Vid6_ClaseIndependienteMonitor import Monitor
from mundo_pc.Clase17_7_Vid7_ClaseIndepComputadora import Computadora
from mundo_pc.Clase17_8_Vid8_ClaseIndependienteOrden import Orden

teclado1 = Teclado('HP', 'USB')
monitor1 = Monitor('HP', '15 Pulgadas')
raton1 = Raton('HP', 'USB')
computadora1 = Computadora('HP', monitor1, teclado1, raton1)


teclado2 = Teclado('Acer', 'USB')
monitor2 = Monitor('Samsung', '25 Pulgadas')
raton2 = Raton('HP', 'USB')
computadora2 = Computadora('HP', monitor2, teclado2, raton2)

teclado3 = Teclado('Gamer', 'Bluetooth')
monitor3 = Monitor('Acer', '32 Pulgadas')
raton3 = Raton('Gamer', 'Bluetooth')
computadora3 = Computadora('Acer', monitor3, teclado3, raton3)

teclado4 = Teclado('Apple', 'Bluetooth')
monitor4 = Monitor('Apple', '27 Pulgadas')
raton4 = Raton('Apple', 'Bluetooth')
computadora4 = Computadora('Apple', monitor4, teclado4, raton4)

teclado5 = Teclado('Samsung', 'Bluetooth')
monitor5 = Monitor('Samsung', '27 Pulgadas')
raton5 = Raton('Samsung', 'Bluetooth')
computadora5 = Computadora('Samsung', monitor5, teclado5, raton5)

computadora6 = Computadora('Samsung', monitor1, teclado2, raton4)
computadora7 = Computadora('Gamer', monitor2, teclado3, raton5)

computadora1 = [computadora1, computadora2, computadora7, computadora4]
orden1 = Orden(computadora1)
orden1.agregar_computadoras(computadora3)
print(orden1)

computadora2 = [computadora3, computadora5, computadora6]
orden2 = Orden(computadora2)
orden2.agregar_computadoras(computadora1)
print(orden2)