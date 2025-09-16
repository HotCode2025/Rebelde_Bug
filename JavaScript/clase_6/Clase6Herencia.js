class Persona{//Clase padre
    constructor(nombre,apellido){
        this._nombre = nombre;
        this._apellido = apellido;
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
}

class Empleado extends Persona{//clase hija
    constructor(nombre, apellido, departamento){//tenemos que agregar los parámetros de la clase padre
        super(nombre, apellido); //llamamos al constructor de la clase padre
        this._departamento = departamento;
    }
    get departamento(){
        return this._departamento;
    }
    set departamento(departamento){
        this._departamento = departamento;
    }
}

let empleado1 = new Empleado("Maria", "Gimenez", "Sistemas" );
console.log(empleado1);
console.log(empleado1.nombre);//get nombre no existe en la clase empleado, se está heredando de la clase persona (padre)