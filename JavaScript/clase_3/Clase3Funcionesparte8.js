//CONCEPTO DE HOISTING

//función de tipo expresión
let sumar = function(a=4,b=8){//estos valores no quedan si yo luego en los argumentos paso otros distintos que son los que se almacenan en a y b
//es decir los parámetros se sobreescriben con los argumenots que le pasamos a la función    
    console.log(arguments[0]);//muestra el parámetro de a
    console.log(arguments[1]);//muestra el parámetro de b
    return a + b + (arguments[2]);
   
}
resultado = sumar(3,2,9); //le asigno la función sumar a la variable resultado y le paso los argumentos
console.log(resultado)

//EN javascritp SIEMPRE QUE NO USEMOS LA SINTAXIS DE LA FUNCIÓN FLECHA
//PODEMOS APLICAR HOISTING ES DECIR LLAMAR LA FUNCIÓN ANTES DE CREARLA
//En esta función vamos a sumar todos los argumentos
let respuesta = sumarTodo(5,4,13,10,9);//llamamos lafunción
console.log(respuesta);
function sumarTodo(){//definimos la función
    let suma=0;
    for (i = 0; i < arguments.length; i++){
        suma += arguments[i];//arguments es para arreglos
    }
    return suma;
}