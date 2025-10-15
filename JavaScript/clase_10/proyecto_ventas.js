/*
 Sistema de Ventas - Clase 10 
 Objetivo: modelar Productos y Órdenes con agregación.
 Notas: IDs autoincrementales, límite de productos por orden,
 y salida legible con template literals.
*/

//  Clase Producto
class Producto {
  // Contador estático para IDs de productos
  static contadorProductos = 0;

  constructor(nombre, precio) {
    // ID autoincremental por cada nuevo producto
    this._idProducto = ++Producto.contadorProductos;
    this._nombre = nombre;
    // Normalizamos a número; si viene algo raro, queda 0
    this._precio = Number(precio) || 0;
  }

  // Getters
  get idProducto() {
    return this._idProducto;
  }
  get nombre() {
    return this._nombre;
  }
  get precio() {
    return this._precio;
  }

  // Setters
  set nombre(nombre) {
    this._nombre = String(nombre);
  }
  set precio(precio) {
    // Validación simple para evitar valores inválidos
    const n = Number(precio);
    if (Number.isNaN(n) || n < 0)
      throw new Error("El precio debe ser un número >= 0");
    this._precio = n;
  }

  // Representación
  toString() {
    // Usamos template literal para formatear el texto
    return `Producto { id: ${this._idProducto}, nombre: "${
      this._nombre
    }", precio: $${this._precio.toFixed(2)} }`;
  }
}

//  Clase Orden
class Orden {
  // Contador estático para IDs de órdenes
  static contadorOrdenes = 0;
  //  una orden admite hasta 5 productos
  static MAX_PRODUCTOS = 5;

  constructor() {
    this._idOrden = ++Orden.contadorOrdenes;
    // Almacena instancias de Producto
    this._productos = [];
    // cuántos intentos de agregado se hicieron
    this._contadorProductosAgregados = 0;
  }

  // Getters
  get idOrden() {
    return this._idOrden;
  }
  // Devolvemos copia para evitar mutaciones externas del array interno
  get productos() {
    return [...this._productos];
  }
  get contadorProductosAgregados() {
    return this._contadorProductosAgregados;
  }

  // Agrega un producto respetando el tipo y el máximo permitido
  agregarProducto(producto) {
    // aseguramos que sea un Producto real
    if (!(producto instanceof Producto)) {
      throw new Error("Solo se pueden agregar instancias de Producto");
    }
    // Regla de capacidad
    if (this._productos.length >= Orden.MAX_PRODUCTOS) {
      console.warn(
        `Orden #${this._idOrden}: ya alcanzó el máximo de ${Orden.MAX_PRODUCTOS} productos.`
      );
      return false; // señalamos que no se pudo
    }
    this._productos.push(producto);
    this._contadorProductosAgregados++;
    return true; // agregado OK
  }

  // Suma el precio de todos los productos de la orden
  calcularTotal() {
    return this._productos.reduce((acc, p) => acc + p.precio, 0);
  }

  // Muestra un resumen
  mostrarOrden() {
    const cabecera = `\n===== Orden #${this._idOrden} =====`;
    const listado = this._productos.length
      ? this._productos.map((p) => ` - ${p.toString()}`).join("\n")
      : " (sin productos)";
    const total = `Total: $${this.calcularTotal().toFixed(2)}`;
    const resumen = `Items: ${this._productos.length}/${Orden.MAX_PRODUCTOS}`;

    const salida = `${cabecera}\n${listado}\n${resumen}\n${total}\n======================\n`;
    console.log(salida);
    return salida; 
  }
}

//  VentasTest
(() => {
  // Creamos algunos productos de ejemplo
  const p1 = new Producto("Galletitas", 950);
  const p2 = new Producto("Gaseosa 1.5L", 1800.5);
  const p3 = new Producto("Caramelos", 250.75);
  const p4 = new Producto("Yerba 1kg", 3500);
  const p5 = new Producto("Azúcar 1kg", 1200);
  const p6 = new Producto("Leche 1L", 950); // sirve para probar el límite
  let productos = [p1, p2, p3, p4, p5, p6];

  // Mostramos los productos creados
  console.log(
    "Productos disponibles:" +
      productos.map((p) => `\n${p.toString()}`).join("") +
      "\n"
  );

  // Orden 1: agregamos 3 productos y mostramos
  const orden1 = new Orden();
  orden1.agregarProducto(p1);
  orden1.agregarProducto(p2);
  orden1.agregarProducto(p3);
  orden1.mostrarOrden();

  // Orden 2: probamos el límite MAX_PRODUCTOS (el 6° no entra)
  const orden2 = new Orden();
  [p1, p2, p3, p4, p5, p6].forEach((p) => orden2.agregarProducto(p));
  orden2.mostrarOrden();

  
  p3.precio = 300; // actualizamos precio de un producto
  console.log(`Actualizado: ${p3.toString()}`);
})();
