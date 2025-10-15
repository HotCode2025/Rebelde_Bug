/*
clase 9
9.4 Creación de la Clase Cliente
*/

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