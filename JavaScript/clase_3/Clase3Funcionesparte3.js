//FUNCIONES DE TIPO EXPRESIÓN
//Declaramos una función de tipo expresión o anónima
//Asignamos la función a una variable
let x = function(a,b){return a+b};//necesitamos poner ; porque la función va en una sola línea y necesita ser cerrada
resultado = x(5,6);//al llamarla se pone la variabel y paréntesis, en los paréntesis pasamos los argumentos para la función anónima
console.log(resultado);
//función anónima porque no tiene nombre, no es necesario, para eso usamos una variable (x) y el resultado se lo asignamos a la variable resultado y luego imprimimos