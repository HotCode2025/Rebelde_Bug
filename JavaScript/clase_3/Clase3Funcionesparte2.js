//PALABRA RETURN
miFuncion(8,2);//Esto no lo muestra porque no incluimos un console.log

function miFuncion(a,b){//función
    //console.log("Sumamos "+ a + " y " + b + " resultado: "+(a+b));
    return a + b;
}//si no agregamos un return automática// JScript lo agrega en la última línea de nuestra función



//Llamando la función
miFuncion(4,5);//esto no lo muestra porque no hemos puesto un console.log

let resultado = miFuncion(6,7);
console.log(resultado)