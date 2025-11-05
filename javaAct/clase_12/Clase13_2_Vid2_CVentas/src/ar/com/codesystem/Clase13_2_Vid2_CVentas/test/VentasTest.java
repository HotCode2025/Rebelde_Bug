
package ar.com.codesystem.Clase13_2_Vid2_CVentas.test;


import ar.com.codesystem.Clase13_2_Vid2_CVentas.Orden;
import ar.com.codesystem.Clase13_2_Vid2_CVentas.Producto;

public class VentasTest {
    public static void main(String[] args){
        Producto producto1 = new Producto("Pantalon", 9500.00);
        Producto producto2 = new Producto("Campera", 29900.00);
        Producto producto3 = new Producto("Remera", 8500.00);
        Producto producto4 = new Producto("Zapatillas", 45000.00);
        Producto producto5 = new Producto("Cinturón", 6500.00);
        Producto producto6 = new Producto("Gorra", 7000.00);
        Producto producto7 = new Producto("Buzo", 22000.00);
        Producto producto8 = new Producto("Camisa", 12000.00);
        Producto producto9 = new Producto("Medias", 3000.00);
        Producto producto10 = new Producto("Short", 11000.00);
        
        Orden orden1 = new Orden();
        //Agregamos productos al arreglo
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.mostrarOrden();
        
        Orden orden2 = new Orden();
        orden2.agregarProducto(producto1);
        orden2.agregarProducto(producto2);
        orden2.agregarProducto(producto3);
        orden2.agregarProducto(producto4);
        orden2.mostrarOrden();
        
        Orden orden3 = new Orden();
        orden3.agregarProducto(producto5);
        orden3.agregarProducto(producto6);
        orden3.agregarProducto(producto7);
        orden3.agregarProducto(producto8);
        orden3.agregarProducto(producto9);
        orden3.agregarProducto(producto10);
        orden3.mostrarOrden();
        
        //Crear mas objetos de tipo producto = 10
        //Crear mas objetos de tipo orden = 2
        
        
    }
}
