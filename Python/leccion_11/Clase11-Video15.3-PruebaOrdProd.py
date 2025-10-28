from Orden import Orden
from Producto import Producto

producto1 = Producto('Camiseta', 100.00)
producto2 = Producto('Pantalon', 150.00)
producto3 = Producto('Top', 90.00)
producto4 = Producto('Bermuda', 130.00)
producto5 = Producto('Musculosa', 95.00)
producto6 = Producto('Medias', 10.000)
producto7 = Producto('Cinto', 25.000)

productos1 = [producto1, producto2] # Lista de productos
orden1 = Orden(productos1) # Primer objeto orden pasando la lista de productos
orden1.agregar_producto(producto6)
print(orden1)
print(f'Total de la orden1: {orden1.calcular_total()}')

productos2= [producto1, producto3, producto4, producto5]
orden2 = Orden(productos2)
orden1.agregar_producto(producto7)
print(orden2)
print(f'Total de la orden2: {orden2.calcular_total()}')