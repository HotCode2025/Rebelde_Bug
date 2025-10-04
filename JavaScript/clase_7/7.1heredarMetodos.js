// 7.1 Heredar métodos
// 7.2 Sobreescritura
// 7.3 Clase Object, toString, sobreescritura y Polimorfismo

class Persona {
    constructor(nombre, apellido) {
        this._nombre = nombre;
        this._apellido = apellido;
    }

    // Getter y Setter para nombre
    get nombre() {
        return this._nombre;
    }

    set nombre(nombre) {
        this._nombre = nombre;
    }

    //  Getter y Setter para apellido
    get apellido() {
        return this._apellido;
    }

    set apellido(apellido) {
        this._apellido = apellido;
    }
    nombreCompleto() {
        return this._nombre + ' ' + this._apellido;
    }
}
class Empleado extends Persona {
  constructor(nombre, apellido, departamento) {
    // "super" llama al constructor de la clase padre (Persona)
    super(nombre, apellido);
    this._departamento = departamento;
  }

  get departamento() {
    return this._departamento;
  }

  // sobreescritura del método nombreCompleto
  nombreCompleto() { // tiene que tener el mismo nombre que el método de la clase padre
    return super.nombreCompleto() + ', ' + this._departamento;
  }

  set departamento(departamento) {
    this._departamento = departamento;
  }
  tostring() { // regresa un string
    return this.nombreCompleto() + ' ' + this._departamento;
  }
}

// Crear una instancia
let persona1 = new Persona("Pepe", "Gómez");

//  Modificar el apellido con el setter
persona1.apellido = "Martínez";

//  Mostrar el apellido actualizado con el getter
console.log("Apellido actualizado:", persona1.apellido); 
// salida: Apellido actualizado: Martínez
console.log("Nombre completo:", persona1.nombreCompleto());
let empleado1 = new Empleado("María", "Sir", "Control");

// Ver el objeto completo
console.log(empleado1);

// Acceder a valores con getters
console.log("Nombre:", empleado1.nombre);       // salida: María
console.log("Departamento:", empleado1.departamento); // salida: Control

// obtect. prototype.toString esta es la manera de acceder a atibutos y medodos de manera dinamica
console.log(empleado1.toString());
console.log(persona1.toString()); 
