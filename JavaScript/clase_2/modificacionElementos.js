// Modificamos los elementos del arreglo
autos[1] = 'Nissan';
console.log(autos[1]);

//Agregamos nuevos valores al arreglo
autos.push('Renault'); //Agregamos el elemento al final del arreglo
console.log(autos);

//Otras formas de agregar elemntos al arreglo
autos[autos.length] = 'Volkswagen';
console.log(autos);

//Tercera forma de agregar elementos teniendo CUIDADO
autos[60] = 'Ford';
console.log(autos);



