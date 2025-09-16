class Persona{//creación de la clase persona
    constructor(nombre,apellido){
        this._nombre = nombre;
        this._apellido = apellido;
    }
//para acceder a un atributo ej. nombre
//get o set se usa para poder leer la información de un atributo
//también se usa el método set para poder modificar el valor de un atributo
//el método get no se puede llamar igual que nuestra propiedad, se acostumbra a usar guión bajo antes del nombre de la propiedad o atributo
//METODOS GET Y SET
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
