let x = 10;//variable de tipo primitiva
console.log(x.lenght);
//x no tiene ningún dato asociado por eso la función lenght aparece como undefined

//Objeto
let persona = {//esto crea un objeto en memoria, y este objeto tiene una referencia en memoria
    nombre: "Carlos",
    apellido: "Gil",
    email: "cgil@gmail.com",
    edad: 30,
    nombreCompleto: function(){//método o función en JavaScript
        return this.nombre+" "+this.apellido;
        //creamos este método nombreCompleto dentro del objeto persona como si fuera una propiedad
        //this es un apuntador, apunta al objeto, no puede apuntar a persona porque es una variable que se ha definido fuera del objeto que está entre {}
    }//si ponemos aquí una coma , podríamos seguir agregando debajo propiedades o atributos, ó métodos o funciones, método o función es lo mismo
}

console.log(persona.nombre);//a través de la variable persona accedemos a el espacio de memoria creado para el objeto y donde están guardadas las propiedades (nombre, apellido, etc)
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);
console.log(persona.nombreCompleto());//llamamos a la función con . luego el nombre de la función y no olvidad los ()