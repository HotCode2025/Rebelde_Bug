let x = 10;//variable de tipo primitiva
console.log(x.lenght);
//x no tiene ningún dato asociado por eso la función lenght aparece como undefined
console.log("Tipos primitivos");
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
console.log("Ejecutando con un objeto");
let persona2 = new Object();//Debe crear un nuevo objeto en memoria
persona2.nombre = "Juan";
persona2.direccion = "Salada 14";
persona2.telefono = "5492618282821";
console.log(persona2.telefono);
console.log("Creamos un nuevo objeto");
//muy importante recordar que JAVA SCRIPT es sensible a MAYÚSCULAS Y MINÚSCULAS
console.log(persona["apellido"]);//Accedemos como si fuera un arreglo

console.log("Usamos un ciclo for in");
//for in y accedemos al objeto como si fuera un arreglo
for(propiedad in persona){
    console.log(propiedad);//aquí accedemos a las propiedades pero no a sus valores o contenido (nombre, apellido, etc)
    console.log(persona[propiedad]);//aquí accedemos al contenido de las propiedades (Carlos, Gil, etc)
}
console.log("Cambiamos y elliminamos un error");
//persona.apellido = "Betancud";//Cambiamos dinámicamente un valor del objeto
persona.apellida = "Betancud"//si creamos por ej. por error la propiedad apellida
console.log(persona);
delete persona.apellida;//eliminamos la propiedad apellida y su contenido
console.log(persona);
