//Funciones de tipo self y invoking
(function(a, b){
    console.log("Ejecutando la funcion: "+ (a + b));

    
})(9, 6);

console.log(typeof miFuncion);

function miFuncionDos(a, b){
    console.log(arguments.length);
    
}
miFuncionDos(5, 7, 3, 6);


//tostring
var miFuncionTexto = miFuncionDos.toString();
console.log(miFuncionTexto);