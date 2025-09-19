let x = 10;//variable de tipo primitiva
console.log(x.lenght);
//x no tiene ningún dato asociado por eso la función lenght aparece como undefined
console.log("Tipos primitivos");
//Objeto
let persona = {//esto crea un objeto en memoria, y este objeto tiene una referencia en memoria
    nombre: "Carlos",
    apellido: "Gil",
    email: "cgil@gmail.com",
    edad: 28,
    idioma: "es",
     get lang(){
        return this.idioma.toUpperCase();//convierte minúscula a mayúscula
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();//recibe el parámetro lang y lo convierte a mayúscula con toUpperCase y recién ahí se lo asigna a la propiedad idioma
    },
    nombreCompleto: function(){//método o función en JavaScript
        return this.nombre+" "+this.apellido;
        //creamos este método nombreCompleto dentro del objeto persona como si fuera una propiedad
        //this es un apuntador, apunta al objeto, no puede apuntar a persona porque es una variable que se ha definido fuera del objeto que está entre {}
    },//si ponemos aquí una coma , podríamos seguir agregando debajo propiedades o atributos, ó métodos o funciones, método o función es lo mismo
    get nombreEdad(){//este es el método get, hay que poner la coma en la { anterior
        return "El nombre es: "+this.nombre+", Edad: "+this.edad;
    }
   
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

//Distintas formas de imprimir un objeto
//Número 1: la más sencilla: concatenar cada valor de cada propiedad
console.log("Distinta formas de imprimir un objeto: forma 1");
console.log(persona.nombre+" , "+persona.apellido);

//Número 2: A través del ciclo for in
console.log("Distinta formas de imprimir un objeto: forma 2");
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}

//Número 3: La función Objetct.values()
//este es un método que nos regresa nuestro objeto pero como un arreglo
console.log("Distinta formas de imprimir un objeto: forma 3");
let personaArray = Object.values(persona);//creamos la variable personaArray
console.log(personaArray);

//Número 4: Utilizaremos el método JSON.stringify
console.log("Distinta formas de imprimir un objeto: forma 4");
let personaString = JSON.stringify(persona);//el método stringify trasnforma en contenido de nuestro objeto, cada una de las propiedades de nuestro objeto en una cadena de string 
console.log(personaString);

// ---------------- MÉTODOS GET Y SET ---------------
//VIDEO 5.1
//get significa obtener, nos permite acceder al valor de nuestras propiedades
console.log("Comenzamos a utilizar el método get");
console.log(persona.nombreEdad);
console.log("Comenzamos con el método get y set para idiomas");
persona.lang = "en";
console.log(persona.lang);
//set su utiliza para que el método pueda ser moficado

// ------- CONSTRUCTORES DE OBJETOS ----------
//VIDEO 5.2
function Persona3(nombre, apellido, email){//función Constructor que la usamos para crear objetos de tipo persona de manera similar a cdo creamos el objeto Persona
    //los parámetros van entre los () y van a ser los atributos de nuestros objetos y pueden llevar un valor preasignado (en este caso nombre)
    //function Persona3(nombre = "Luis", apellido, email)
    //la ventaja es que podemos crear varios objetos de tipo Persona no solamente uno
    this.nombre = nombre;//la palabra this dentro de la función nos va a permitir trabajar con las propiedades del objeto que se está ejecutando
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){//Aquí estamos creando un método dentro del método constructor
        return this.nombre+" "+this.apellido;
    }
}
let padre = new Persona3("Leo", "Lopez", "lopezl@gmail.com");//es un método para la creación de objetos
//la palabra reservada new se usa para crear el nuevo objeto
padre.nombre = "Luis";//modificamos el nombre
padre.telefono = "5492618282821";//una propiedad exclusiva del objeto padre
console.log(padre);
console.log(padre.nombreCompleto());//utilizamos la función
let madre = new Persona3("Laura", "Contreras", "contreral@gmail.com");
console.log(madre);
console.log(madre.telefono);//la propiedad no está definida
console.log(madre.nombreCompleto());
//cada vez que usamos new se crea un nuevo objeto del mismo tipo

// ------------- AGREGAR MÉTODOS AL CONSTRUCTOR OBJETO -----------------
// VIDEO 5.3
//this.nombreCompleto = function(){//Aquí estamos creando un método dentro del método constructor
//        return this.nombre+" "+this.apellido;
//    }
//console.log(madre.nombreCompleto());

// --------------- Distintas formas de crear objetos ----------------------
//VIDEO 5.4 
// Caso ojbeto 1
let miObjeto = new Object();//Esta es una opción formal
// Caso ojbeto 2
let miObjeto2 = {};//Esta opción es breve y recomendada

// Caso String 1
let miCadena1 = new String("Hola");//sintaxis formal
// Caso String 2
let miCadena2 = "Hola";//Esta es la sintaxis simplificada y recomendada

//caso con números 1
let miNumero = new Number(1);//es formal y no recomendable, esto sería la función constructora para objeto con números
//caso con números 2
let miNumero2 = 1;//sintaxis recomendada

//caso boolean 1
let miBoolean1 = new Boolean(false);//formal
//caso boolean 2
let miBoolean2 = false;//sintaxis recomendada

//caso Arreglos 1
let miArreglo1 = new Array();//formal
//caso Arreglos 2
let miArreglo2 = [];//sintaxis recomendada, aquí creamos un arreglo vacío

//caso function 1
//let miFunction1 = new function();//todo después de new es considerado objeto
//caso function 2
let miFunction2 = function(){};//notación simplificada y recomendada

// -------------------- El uso de prototype -------------------------- 
//VIDEO 5.5
Persona3.prototype.telefono = "2618338659";
console.log(padre);
console.log(madre);
madre.telefono = "5492618338659";

// -------------------- El uso de call -------------------------- 
//VIDEO 5.6
//el método call nos va a permitir llamar a un método que está definido en un objeto desde otro objeto 
// -------------------- El uso de apply -------------------------- 
let persona4 = {
    nombre: "Juan",
    apellido: "Perez",
    nombreCompleto2: function(titulo, telefono){//titulo y teléfono son parámetros
        return titulo+": "+this.nombre+ " "+this.apellido+" "+telefono;
    }
}

let persona5 ={
    nombre: "Carlos",
    apellido: "Lara"
}//no hemos definido dentro del objeto persona5 el método nombreCompleto2 pero vamos a poder hacer uso de ese método con la función call
console.log(persona4.nombreCompleto2("Lic.", "5492618484845"));//aquí pasamos como argumentos Lic y 5492618484845
console.log(persona4.nombreCompleto2.call(persona5, "Ing.", "5492618585856"));
//a través de la función call ingresamos en los paréntesis, primero el objeto (persona5) que no tiene el método nombreCompleto2
//y luego simplemente pasamos los argumentos separados por comas 

// ------------------------ El método apply -------------------------
//VIDEO 5.7
let persona6 = {
    nombre: "Sofia",
    apellido: "Mendez",
    nombreCompleto2: function(){
        return this.nombre+ " "+this.apellido;
    }
}
console.log(persona6.nombreCompleto2());

console.log(persona4.nombreCompleto2.call(persona6, "Ing.", "5492618585856"));

console.log(persona6.nombreCompleto2.apply(persona5));

//Metodo Apply
let arreglo = ["Ing.", "5492618686865"];//cdo utilizamos apply en lugar de pasar argumentos pasamos un arreglo con todos los valores de los argumentos que deseaamos pasar a nuestro método en este caso el método es nombreCompleto2
console.log(persona4.nombreCompleto2.apply(persona5,arreglo));
//apply lee el arreglo y pasa los valores como argumentos a nombreCompleto2

