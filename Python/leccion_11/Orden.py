from Producto import Producto


class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self.id_orden = Orden.contador_ordenes
        self._productos = list(productos)
    def agregar_producto(self, producto):
        self._productos.append(producto) # Esto es para agregar un nuevo producto

    def calcular_total(self):
        total = 0 # variable temporal para almacenar el total temporal porque tomamos el valor parcial que vamos obteniendo de cada producto
        for producto in self._productos:
            total += producto.precio
        return total
    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__()+' | '
        return f'Orden_ {self.id_orden}, \nProducto: {productos_str}'
if __name__ == '__main__':
    producto1 = Producto('Camiseta', 100.00)
    producto2 = Producto('Pantalon', 150.00)
    producto3 = Producto('Top', 90.00)
    producto4 = Producto('Bermuda', 130.00)
    producto5 = Producto('Musculosa', 95.00)
    productos1 = [producto1, producto2] # Lista de productos
    productos2= [producto1, producto3, producto4, producto5]
    orden1 = Orden(productos1) # Primer objeto orden pasando la lista de productos
    print(orden1)
    orden2 = Orden(productos2)
    print(orden2)
# Tarea: Modificar la orden2 ingresando nuevos productos con sus nombres y precios
# Crear una nueva lista de productos y agregarla a la orden 2