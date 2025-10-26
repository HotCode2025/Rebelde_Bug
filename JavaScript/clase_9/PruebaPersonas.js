//9.5 Cargando todo en una misma plantilla

class Persona {
    static contadorPersonas = 0;
    constructor(nombre, apellido, edad){
        this._idPersona = ++Persona.contadorPersonas;
        this._nombre = nombre;
        this._apellido = apellido;
        this._edad = edad;
    }

    get idPersona(){
        return this._idPersona;
    }

    get nombre(){
        return this._nombre;
    }

    set nombre(nombre){
        this._nombre = nombre;
    }

    get apellido(){
        return this._apellido;
    }

    set apellido(apellido){
        this._apellido = apellido;
    }

    get edad(){
        return this._edad;
    }

    set edad(edad){
        this._edad = edad;
    }

    toString(){
        return `ID: ${this._idPersona}, 
                Nombre: ${this._nombre}, 
                Apellido: ${this._apellido}, 
                Edad: ${this._edad}`;
    }

}

class Empleado extends Persona{

    static contadorEmpleados = 0;

    constructor(nombre, apellido, edad, salario){
        super(nombre, apellido, edad);
        this._idEmpleado = ++Empleado.contadorEmpleados;
        this._salario = salario;
    }

    get idEmpleado(){
        return this._idEmpleado;
    }

    get salario(){
        return this._salario;
    }

    set salario(salario){
        this._salario = salario;
    }

    toString(){
        return `${super.toString()},
                ID Empleado: ${this._idEmpleado},
                Salario: ${this._salario}`;
    }
}

class Cliente extends Persona{

    static contadorClientes = 0;

    constructor(nombre, apellido, edad, fechaRegistro){
        super(nombre, apellido, edad);
        this._idCliente = ++Cliente.contadorClientes;
        this._fechaRegistro = fechaRegistro;
    }

    get idCliente(){
        return this._idCliente;
    }

    get fechaRegistro(){
        return this._fechaRegistro;
    }

    set fechaRegistro(fechaRegistro){
        this._fechaRegistro = fechaRegistro;
    }

    toString(){
        return `${super.toString()},
                ID Cliente: ${this._idCliente},
                Fecha de Registro: ${this._fechaRegistro}`;
    }
}

// 9.6 Prueba clase Persona
let persona1 = new Persona('Juan', 'Pérez', 28);
console.log(persona1.toString());

let persona2 = new Persona('Ana', 'Gómez', 34);
console.log(persona2.toString());

// 9.7 Prueba clase Empleado
let empleado1 = new Empleado('Carlos', 'López', 30, 50000);
console.log(empleado1.toString());

let empleado2 = new Empleado('María', 'Rodríguez', 25, 60000);
console.log(empleado2.toString());