/*
clase 9
9.3 Creación de la Clase Empleado
*/

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
