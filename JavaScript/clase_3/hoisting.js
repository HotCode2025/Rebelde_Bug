// Hoisting en funciones
// En JavaScript, las funciones declaradas con "function" se cargan primero.
// Eso permite llamarlas ANTES de que aparezcan en el código (esto se llama HOISTING).

// Aquí llamamos la función "suma" antes de declararla.
let resultado = suma(3, 4, 5, 13, 9);
console.log("Resultado:", resultado); // salida: 34

// Declaración de la función
function suma() {
    let total = 0;

    // El objeto "arguments" contiene todos los valores pasados
    // aunque no hayamos definido parámetros.
    for (let i = 0; i < arguments.length; i++) {
        total += arguments[i]; // vamos sumando cada argumento
    }

    return total; // devolvemos la suma total
}