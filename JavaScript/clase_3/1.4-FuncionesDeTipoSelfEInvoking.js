//Funciones de tipo self e invoking
(function (a, b){
    console.log('Ejecutando la función: ' + (a + b));
})(9, 6);

console.log(typeof miFuncion);
function miFuncionDos(a, b){
    console.log(arguments.length);
}

miFuncionDos(5, 7, 3, 6);