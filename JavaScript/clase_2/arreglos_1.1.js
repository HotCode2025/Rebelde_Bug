//1.1 Arreglos en JavaScript

// Forma antigua de crear arrays (NO recomendada)
// Usar "new Array()" puede dar resultados inesperados, especialmente con un solo número.
// Ejemplo: new Array(3) crea un array vacío con 3 posiciones, NO el número 3.
let autos1 = new Array('BMW', 'Audi', 'Volvo');
console.log("Array con forma antigua:", autos1);

// Forma moderna y recomendada
// Usar corchetes [] es más claro, seguro y usado en la práctica.
const autos2 = ['BMW', 'Audi', 'Volvo'];
console.log("Array con forma recomendada:", autos2);
