// while repite un bloque de código mientras la condición sea verdadera..
let contador = 0;
while (contador < 5) {
    console.log("Contador:", contador);
    contador++;
}
console.log("Fin del ciclo while");

/*
Evalúa la condición..

Si es true, ejecuta el código dentro...

Vuelve a evaluar.

Se detiene cuando la condición es false
*/

// do while ejecuta el bloque al menos una vez antes de evaluar la condición.
let conteo = 0;
do {
    console.log("Conteo:", conteo);
    conteo++;
} while (conteo < 5);
console.log("Fin del ciclo do while");

// ciclo for itera un número específico de veces.
for (let contando = 0; contando < 5; contando++) {
    console.log("Contando:", contando);
}

console.log("Fin del ciclo for");

// palabra reservada break para salir de un ciclo.
for (let contando = 0; contando <= 10; contando++) {
    if (contando % 2 == 0) {
        console.log("Contando (par):", contando);
        break; // sale del ciclo al encontrar el primer número par
    }
}
console.log("Fin del ciclo con break");


// palabra reservada continue para saltar a la siguiente iteración y etiquetas labels 
inicio:
for (let contando = 0; contando <= 10; contando++) {
    if (contando % 2 !== 0) {
        continue inicio; // salta los números impares
    }
    console.log("Contando (par):", contando);
}



