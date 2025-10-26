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