// 12.1 Manejo de Matrices Parte 1: Aquí creamos la carpeta Leccion10
// 12.2 Manejo de Matrices Parte 2: Hacer la tarea
// 12.3 Manejo de Matrices Parte 3: Ciclo for iterando
// 12.4 Manejo de Matrices Parte 4: Sintaxis simplificada
// 12.5 Manejo de Matrices Parte 5: Matriz de objetos, creamos un método

package javaAct.clase_11;

/**
 * Clase de prueba (Test) para el manejo de Arreglos Bidimensionales (Matrices).
 * Muestra la creación, inicialización y recorrido de matrices
 * con primitivos (int), Strings y Objetos (Persona).
 */
public class TesMatrices {

    public static void main(String[] args) {
        
        // 1. Matriz de tipo primitivo (int)
        // Se declara una matriz de 2 filas y 3 columnas.
        int edades[][] = new int[2][3];
        
        System.out.println("Referencia de memoria de la matriz: " + edades);
        System.out.println("Número de filas: " + edades.length);
        System.out.println("Número de columnas (fila 0): " + edades[0].length);

        // Asignación de valores
        edades[0][0] = 10;
        edades[0][1] = 20;
        edades[0][2] = 30;
        edades[1][0] = 40;
        edades[1][1] = 50;
        edades[1][2] = 60;

        System.out.println("--- Recorriendo matriz de edades con bucles anidados ---");
        // Bucle externo: recorre las filas
        for (int fila = 0; fila < edades.length; fila++) {
            // Bucle interno: recorre las columnas de la fila actual
            for (int col = 0; col < edades[fila].length; col++) {
                System.out.println("Edad en [" + fila + "][" + col + "]: " + edades[fila][col]);
            }
        }

        System.out.println("----------------------------------------");

        // 2. Matriz de String (Sintaxis simplificada)
        String frutas[][] = {{"Manzana", "Banana"}, {"Cereza", "Durazno"}};
        
        System.out.println("--- Recorriendo matriz de frutas ---");
        for (int i = 0; i < frutas.length; i++) {
            for (int j = 0; j < frutas[i].length; j++) {
                System.out.println("Fruta en [" + i + "][" + j + "]: " + frutas[i][j]);
            }
        }

        System.out.println("----------------------------------------");

        // 3. Matriz de Objetos (Persona)
        Persona personas[][] = new Persona[2][2];
        personas[0][0] = new Persona("Ana");
        personas[0][1] = new Persona("Luis");
        // CORRECCIÓN: Se añaden las instancias que faltaban
        personas[1][0] = new Persona("Maria"); 
        personas[1][1] = new Persona("Juan");

        // CORRECCIÓN: Se llama al método auxiliar para que se ejecute
        System.out.println("--- Recorriendo matriz de personas (con método) ---");
        imprimirMatrizPersonas(personas);
    }

    /**
     * Método estático auxiliar para imprimir una matriz de objetos Persona.
     * @param matriz La matriz de Persona a imprimir.
     */
    public static void imprimirMatrizPersonas(Persona matriz[][]) {
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                // Se usa getNombre() para acceder al dato.
                // También se podría imprimir solo 'matriz[i][j]' gracias
                // al método toString() que agregamos en Persona.java
                System.out.println("Persona en [" + i + "][" + j + "]: " + matriz[i][j].getNombre());
            }
        }
    }
}