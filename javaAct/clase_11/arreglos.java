// 11.1 Arreglos Parte 1: Creamos la carpeta Leccion9
// 11.2 Arreglos Parte 2
// 11.3 Arreglos Parte 3


package javaAct.clase_11;

/**
 * Clase de demostración para los fundamentos de Arreglos (Arrays)
 * con tipos de datos primitivos (int).
 */
public class arreglos {
    
    // El método main es 'static' y es el punto de entrada de la aplicación.
    public static void main(String[] args) {
        
        // 1. Declaración e Inicialización
        // Se crea un arreglo de enteros con un tamaño fijo de 3.
        // Los valores por defecto se inicializan en 0.
        int edades[] = new int[3];
        
        // 2. Impresión incorrecta vs. correcta
        // System.out.println("Referencia de memoria: " + edades); // Imprime algo como [I@1f32e575
        System.out.println("Tamaño del arreglo (length): " + edades.length); // Imprime 3

        // 3. Asignación de valores por índice
        // Los índices en Java comienzan en 0.
        edades[0] = 10;
        System.out.println("Edad en la posición 0: " + edades[0]);

        edades[1] = 20;
        System.out.println("Edad en la posición 1: " + edades[1]);

        edades[2] = 30;
        System.out.println("Edad en la posición 2: " + edades[2]);

        // 4. Error común (comentado para evitar que falle)
        // Intentar acceder a un índice fuera del límite (0, 1, 2)
        // produce una excepción: ArrayIndexOutOfBoundsException
        // edades[3] = 40; 

        // 5. Recorrido del arreglo con un bucle 'for'
        System.out.println("--- Recorriendo el arreglo con un bucle for ---");
        for (int i = 0; i < edades.length; i++) {
            System.out.println("Edad en la posición " + i + ": " + edades[i]);
        }
    }
}
