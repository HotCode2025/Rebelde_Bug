//PASO POR VALOR
//Es cdo usamos tipos que no soy objetos, tipos numéricos tipos booleanos, etc
//al asignar un valor numérico a una variable se lo conoce como valor primitivo
//porque no tiene propiedades ni métodos

//TIPOS PRIMITIVOS
let x=10;//esta variable es global
function cambiarValor(a){//PASO POR VALOR
    //aquí aunque se llame a le estamos pasando el valor de x
    a=20;//esta variable la creamos acá sólo tiene efecto dentro de esta estructura que es la función, NO es global
//entonces primero recibe el valor de 10 y luego lo cambiamos a 20 pero esto dentro de la estructura
//pero no se está modificando el espacio de memoria de la variable x que hemos creado global
//porque la variable creada dentro de la estructura es otra variable distinta y tiene otro espacio de memoria
}
//cdo se terminó la función la varible a, a la cual le asignamos 20 se destruyó
//y la varible x que estaba afuera no se modificó, sigue valiendo 10
cambiarValor(x);
console.log(x);
//Aunque no colocamos return el programa lo hace solo

//IMPORTANTE: en el paso por valor la variable no sufre cambios en este caso X