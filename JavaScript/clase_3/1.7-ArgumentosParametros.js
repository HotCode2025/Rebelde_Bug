//To String
var miFuncionTexto = miFuncionDos.toString();
console.log(miFuncionTexto);

//Funciones flecha
const sumarFuncionFlecha = (a, b) => a + b;
resultado = sumarFuncionFlecha(3, 7); //Asignamos el valor a una variable
console.log(resultado);

let sumar = function(a = 4, b = 8){
    console.log(arguments[0]); //Muestra el parámetro de a:
    console.log(arguments[1]); //Muestra el parámetro de b:
    a + b + arguments[2];
    return a + b;
}
resultado = sumar(3, 2, 9);
console.log(resultado);

//Sumar todos los argumentos
let respuesta = sumarTodo(5, 4, 13, 10, 9);
console.log(respuesta);
function sumarTodo(){
    let suma = 0;
    for(let i = 0; i < arguments.length; i++){
        suma+= arguments[i]; //arguments es para arreglos
    }
    return suma;
}
