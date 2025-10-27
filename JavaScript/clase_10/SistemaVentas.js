// video 10.3 Prueba de la Clase Producto

class Producto {
    static contadorProductos = 0;
    constructor(nombre, precio) {
        this.idProducto = ++Producto.contadorProductos;
        this.nombre = nombre;
        this.precio = precio;
    }
    
    get getIdProducto() {
        return this.idProducto;
    }

    get getNombre() {
        return this.nombre;
    }

    set setNombre(nombre) {
        this.nombre = nombre;
    }

    get getPrecio() {
        return this.precio;
    }

    set setPrecio(precio) {
        this.precio = precio;
    }

    toString() { //Template Literal: nos permite insertar código de forma dinámica
        return `ID: ${this.idProducto}, Nombre: ${this.nombre}, Precio: ${this.precio}`;
    }
} //Fin clase Producto

// video 4

class Orden {
    static contadorOrdenes = 0;
    static get MAX_PRODUCTOS() { //Simular una constante
        return 5;
    }

    constructor() {
        this.idOrden = ++Orden.contadorOrdenes;
        this.productos = [];
        this.contadorProductosAgregados = 0;
    }

    get getIdOrden() {
        return this.idOrden;
    }

    agregarProducto(producto) {
        if (this.productos.length < Orden.MAX_PRODUCTOS) {
            this.productos.push(producto); // Tenemos dos tipos de sintaxis: 1
            //this.productos[this.contadorProductosAgregados++] = producto; // segunda sintaxis
            this.contadorProductosAgregados++;
        } else {
            console.log('No se pueden agregar más productos a la orden');
        }
    } // Fin del método agregarProducto

    // 10.5 Pruebas con la relación de Agregación
    calcularTotal() {
        let totalVenta = 0;
        for (let producto of this.productos) {
            totalVenta += producto.getPrecio;
        } // Fin del ciclo for
        return totalVenta;
    } // Fin del método calcularTotal

    mostrarOrden() {
        let productosOrden = '';
        for (let producto of this.productos) {
            productosOrden += '\n{' + producto.toString() + '} ';
        } // Fin del ciclo for
        console.log(`Orden: ${this.idOrden}, Total: $${this.calcularTotal()}, Productos: ${productosOrden}`);
    } // Fin del método mostrarOrden
} // Fin de la clase Orden



let producto1 = new Producto('Camisa', 500);
let producto2 = new Producto('Pantalón', 700);
let producto3 = new Producto('Chamarra', 1500);

// 10.5 Pruebas con la relación de Agregación (video 6)

let orden1 = new Orden();
orden1.agregarProducto(producto1);
orden1.agregarProducto(producto2);
orden1.agregarProducto(producto3);
orden1.mostrarOrden();

let orden2 = new Orden();
orden2.agregarProducto(producto1);
orden2.agregarProducto(producto2);
orden2.agregarProducto(producto3);
orden2.mostrarOrden();

// Prueba del límite de productos por orden
let orden3 = new Orden();
orden3.agregarProducto(producto1);
orden3.agregarProducto(producto2);
orden3.agregarProducto(producto3);
orden3.agregarProducto(producto1);
orden3.mostrarOrden();
orden3.agregarProducto(producto2); // 5to producto
orden3.agregarProducto(producto3); // 6to producto - Debe mostrar un mensaje de error

