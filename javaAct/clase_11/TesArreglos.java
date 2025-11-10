
package javaAct.clase_11;

// Se importa la clase Persona para poder usarla.
import javaAct.clase_11.Persona;

/**
 * Clase de prueba (Test) para demostrar el uso de Arreglos con Objetos (Persona)
 * y la sintaxis de inicialización simplificada (String).
 */
public class TesArreglos {
    public static void main(String[] args) {
        
        // 1. Arreglo de Objetos (Persona)
        // Se crea un arreglo para 3 objetos de tipo Persona.
        // Inicialmente, contiene [null, null, null].
        Persona personas[] = new Persona[3];

        // Se crean los objetos (instancias) y se asignan a cada índice.
        personas[0] = new Persona("Ana");
        personas[1] = new Persona("Luis");
        personas[2] = new Persona("Maria");

        System.out.println("--- Lista de personas (acceso manual) ---");
        System.out.println("Nombre en la posición 0: " + personas[0].getNombre());
        System.out.println("Nombre en la posición 1: " + personas[1].getNombre());
        System.out.println("Nombre en la posición 2: " + personas[2].getNombre());

        System.out.println("--- Lista de personas (con bucle for) ---");
        for (int i = 0; i < personas.length; i++) {
            // Gracias al método toString() en Persona.java,
            // al imprimir 'personas[i]', Java automáticamente llama a ese
            // método y muestra el nombre.
            System.out.println("Nombre en la posición " + i + ": " + personas[i]);
        }
        
        System.out.println("----------------------------------------");

        // 2. Arreglo con Sintaxis Simplificada
        // Se declara e inicializa el arreglo en una sola línea.
        String frutas[] = {"Manzana", "Banana", "Cereza"};
        
        System.out.println("--- Lista de frutas (con bucle for) ---");
        for (int j = 0; j < frutas.length; j++) {
            System.out.println("Fruta en la posición " + j + ": " + frutas[j]); 
        }
    }
}