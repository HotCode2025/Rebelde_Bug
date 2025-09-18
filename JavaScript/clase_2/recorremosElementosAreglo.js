//1.2 Recorremos los elementos de un arreglo

const autos = ['BMW', 'Audi', 'Volvo'];
console.log("Array de autos:", autos[0]); // Acceder al primer elemento
console.log("Array de autos:", autos[1]); // Acceder al segundo elemento
console.log("Array de autos:", autos[2]); // Acceder al tercer elemento

for (let i = 0; i < autos.length; i++) {
    console.log("Auto en posición", i, ":", autos[i]);
}