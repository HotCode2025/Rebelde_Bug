/*
clase 9
9.5 Cargando todo en una sola plantilla9.5 Cargando todo en una sola plantilla
9.6 Prueba Clase Persona
9.7 Prueba Clase Empleado
9.8 Prueba Clase Cliente
*/
class persona {
  static contadorPersonas = 0;

  constructor(nombre, apellido, edad) {
    this._idPersona = ++persona.contadorPersonas;
    this._nombre = nombre;
    this._apellido = apellido;
    this._edad = edad;
  }

  get idPersona() {
    return this._idPersona;
  }
  get nombre() {
    return this._nombre;
  }
  set nombre(nombre) {
    this._nombre = nombre;
  }
  get apellido() {
    return this._apellido;
  }
  set apellido(apellido) {
    this._apellido = apellido;
  }
  get edad() {
    return this._edad;
  }
  set edad(edad) {
    this._edad = edad;
  }

  toString() {
    return `idPersona: ${this._idPersona}, nombre: ${this._nombre}, apellido: ${this._apellido}, edad: ${this._edad}`;
  }
}

class empleado extends persona {
  static contadorEmpleados = 0;

  constructor(nombre, apellido, edad, sueldo) {
    super(nombre, apellido, edad);
    this._idEmpleado = ++empleado.contadorEmpleados;
    this._sueldo = sueldo;
  }
  
  get idEmpleado() {
    return this._idEmpleado;
  }
    get sueldo() {
    return this._sueldo;
  }
  set sueldo(sueldo) {
    this._sueldo = sueldo;
  }

  toString() {
    return `${super.toString()}, idEmpleado: ${this._idEmpleado}, sueldo: ${this._sueldo}`;
  }
}

class cliente extends persona {
  static contadorClientes = 0;

  constructor(nombre, apellido, edad, fechaRegistro) {
    super(nombre, apellido, edad);
    this._idCliente = ++cliente.contadorClientes;
    this._fechaRegistro = fechaRegistro;
  }

  get idCliente() {
    return this._idCliente;
  }
  get fechaRegistro() {
    return this._fechaRegistro;
  }
  set fechaRegistro(fechaRegistro) {
    this._fechaRegistro = fechaRegistro;
  }

  toString() {
    return `${super.toString()}, idCliente: ${this._idCliente}, fechaRegistro: ${this._fechaRegistro}`;
  }
}
//Prueba clase persona
let persona1 = new persona("Juan", "Perez", 28);
console.log(persona1.toString());

let persona2 = new persona("Carla", "Gomez", 25);
console.log(persona2.toString());

//Prueba clase empleado
let empleado1 = new empleado("Carlos", "Lara", 35, 50000);
console.log(empleado1.toString());

let empleado2 = new empleado("Ana", "Sanchez", 28, 60000);
console.log(empleado2.toString());

//Prueba clase cliente
let cliente1 = new cliente("Miguel", "Torres", 30, new Date());
console.log(cliente1.toString());

let cliente2 = new cliente("Laura", "Ramirez", 26, new Date());
console.log(cliente2.toString());