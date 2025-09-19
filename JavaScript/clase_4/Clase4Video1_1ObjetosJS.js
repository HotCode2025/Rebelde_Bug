let x = 10;//variable de tipo primitiva
console.log(x.lenght);
//x no tiene ningún dato asociado por eso la función lenght aparece como undefined

//Objeto
let persona = {//esto crea un objeto en memoria, y este objeto tiene una referencia en memoria
    nombre: "Carlos",
    apellido: "Gil",
    email: "cgil@gmail.com",
    edad: 30
}

console.log(persona.nombre);//a través de la variable persona accedemos a el espacio de memoria creado para el objeto y donde están guardadas las propiedades (nombre, apellido, etc)
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);