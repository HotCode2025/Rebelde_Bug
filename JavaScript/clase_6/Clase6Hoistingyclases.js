//let persona3 = new Persona("Carla","Ponce"); esto no se debe hacer: Persona is not defined
//Siempre debemos definir primero la clase y recién después de eso crear los objetos
class Persona{//Creación de la clae
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

let persona1 = new Persona("Martin", "Perez");//constructor del objeto persona1
console.log(persona1.nombre);//con get obtenemos el nombre que le asignamos con el constructor a persona 1 y lo mostramos
persona1.nombre = "Juan Carlos";//a través del set modificamos el nombre
console.log(persona1.nombre);//mostramos el resultado a través del get
console.log(persona1.apellido);//Obtenemos el apellido en persona1
persona1.apellido = "Calderon";//Modificamos el apellido de persona1
console.log(persona1.nombre, persona1.apellido);//mostramos nombre y apellido modificados en persona1
//console.log(persona1);
let persona2 = new Persona("Carlos", "Lara");//constructor del objeto persona2
console.log(persona2.nombre);
persona2.nombre = "Maria Laura";
console.log(persona2.nombre);
console.log(persona2.apellido);
persona2.apellido = "Ontivero";//Modificamos el apellido de persona2
console.log(persona2.nombre, persona2.apellido);//mostramos nombre y apellido modificados en persona2
//console.log(persona2);

//HOISTING Y CLASES
//Cdo trabajamos con clases no se aplica el concepto de hoisting, es decir,
//primero tenemos que definir nuestra clase para poderla usar
//en cambio si trabajamos con funciones podemos primero llamar a la función y luego definir esta función
//ya que para funciones se aplica el hoisting (1ero. llamamos la función luego se crea la función)
//EN CLASES NO SE APLICA EL CONCEPTO DE HOISTING