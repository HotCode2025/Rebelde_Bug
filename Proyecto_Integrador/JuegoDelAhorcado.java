import java.util.Scanner;
import java.util.Random;

/**
 * Proyecto Integrador - Juego del Ahorcado
 * Tecnicatura en Programación -Rebelde Bug
 * 
 * Este programa implementa el clásico juego del ahorcado.
 * Utiliza arreglos, bucles, condicionales y métodos estáticos.
 * Incluye colores ANSI para mejorar la visualización en consola.
 */

public class JuegoDelAhorcado {

    // Códigos ANSI para colores en consola
    public static final String RESET = "\u001B[0m";
    public static final String ROJO = "\u001B[31m";
    public static final String VERDE = "\u001B[32m";
    public static final String AMARILLO = "\u001B[33m";
    public static final String AZUL = "\u001B[34m";
    public static final String CYAN = "\u001B[36m";
    public static final String MAGENTA = "\u001B[35m";

    // -------------------- SUBPROCESOS Y FUNCIONES --------------------

    /** 
     * Muestra el menú de temáticas disponibles 
     */
    public static void mostrarMenuTemas() {
        System.out.println(AZUL + "\n=== TEMÁTICAS DISPONIBLES ===" + RESET);
        System.out.println("1 - Medicina");
        System.out.println("2 - Cine / Series");
        System.out.println("3 - Música");
        System.out.println("4 - Videojuegos");
        System.out.println("5 - Famosos");
    }

    /** 
     * Devuelve el nombre del tema seleccionado por número 
     */
    public static String seleccionarTema(int opcion) {
        switch (opcion) {
            case 1: return "Medicina";
            case 2: return "Cine / Series";
            case 3: return "Música";
            case 4: return "Videojuegos";
            case 5: return "Famosos";
            default: return "General";
        }
    }

    /** 
     * Carga las palabras por temática en una matriz 5x5 
     */
    public static void llenarTemas(String[][] palabras) {
        palabras[0] = new String[]{"pulso", "virus", "sangre", "cirugia", "neurona"};
        palabras[1] = new String[]{"matrix", "avatar", "interstellar", "sherlock", "narnia"};
        palabras[2] = new String[]{"pop", "bach", "violin", "rock", "sintetizador"};
        palabras[3] = new String[]{"zelda", "doom", "sonic", "minecraft", "overwatch"};
        palabras[4] = new String[]{"oprah", "shakira", "einstein", "messi", "madonna"};
    }

    /** 
     * Selecciona una palabra aleatoria según tema y dificultad 
     */
    public static String seleccionarPalabra(String[][] palabras, int fila, int dificultad) {
        Random random = new Random();
        int col = random.nextInt(dificultad); // valor entre 0 y dificultad-1
        return palabras[fila - 1][col]; // fila -1 porque el usuario elige desde 1
    }

    /** 
     * Verifica si una letra ya fue utilizada 
     */
    public static boolean letraYaUsada(String letra, String[] letrasUsadas) {
        for (String l : letrasUsadas) {
            if (letra.equalsIgnoreCase(l)) {
                return true;
            }
        }
        return false;
    }

    /** 
     * Agrega una letra al arreglo de letras usadas 
     */
    public static void agregarLetraUsada(String letra, String[] letrasUsadas) {
        for (int i = 0; i < letrasUsadas.length; i++) {
            if (letrasUsadas[i].equals("")) {
                letrasUsadas[i] = letra;
                break;
            }
        }
    }

    /** 
     * Busca una letra en la palabra y actualiza la palabra adivinada 
     */
    public static boolean buscarLetraEnPalabra(String letra, String palabra, StringBuilder adivinada) {
        boolean encontrada = false;
        for (int i = 0; i < palabra.length(); i++) {
            if (String.valueOf(palabra.charAt(i)).equalsIgnoreCase(letra)) {
                adivinada.setCharAt(i, palabra.charAt(i));
                encontrada = true;
            }
        }
        return encontrada;
    }

    /** 
     * Dibuja el muñeco del ahorcado según la cantidad de errores 
     */
    public static void mostrarMuneco(int errores) {
        System.out.println(AMARILLO);
        switch (errores) {
            case 0:
                System.out.println(" _______");
                System.out.println("|       |");
                System.out.println("|        ");
                System.out.println("|        ");
                System.out.println("|        ");
                break;
            case 1:
                System.out.println(" _______");
                System.out.println("|       |");
                System.out.println("|       O");
                System.out.println("|        ");
                System.out.println("|        ");
                break;
            case 2:
                System.out.println(" _______");
                System.out.println("|       |");
                System.out.println("|       O");
                System.out.println("|       |");
                System.out.println("|        ");
                break;
            case 3:
                System.out.println(" _______");
                System.out.println("|       |");
                System.out.println("|       O");
                System.out.println("|      /|");
                System.out.println("|        ");
                break;
            case 4:
                System.out.println(" _______");
                System.out.println("|       |");
                System.out.println("|       O");
                System.out.println("|      /|\\");
                System.out.println("|        ");
                break;
            case 5:
                System.out.println(" _______");
                System.out.println("|       |");
                System.out.println("|       O");
                System.out.println("|      /|\\");
                System.out.println("|      / ");
                break;
            case 6:
                System.out.println(" _______");
                System.out.println("|       |");
                System.out.println("|       O");
                System.out.println("|      /|\\");
                System.out.println("|      / \\");
                break;
        }
        System.out.println(RESET);
    }

    // -------------------- PROCESO PRINCIPAL --------------------

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        Random random = new Random();

        // Declaración e inicialización de variables
        String[][] palabras = new String[5][5];
        String tema, palabraSecreta, letra;
        int dificultad, opcionTema, errores = 0, vidas = 6;

        // Inicializa el arreglo de letras usadas
        String[] letrasUsadas = new String[26];
        for (int i = 0; i < letrasUsadas.length; i++) {
            letrasUsadas[i] = "";
        }

        // Cargar los temas
        llenarTemas(palabras);

        // Mostrar menú de temas
        mostrarMenuTemas();

        // Solicitar tema al usuario con validación
        System.out.print(CYAN + "Selecciona una temática (1 a 5): " + RESET);
        opcionTema = entrada.nextInt();
        while (opcionTema < 1 || opcionTema > 5) {
            System.out.print(ROJO + "Opción inválida. Elige entre 1 y 5: " + RESET);
            opcionTema = entrada.nextInt();
        }

        tema = seleccionarTema(opcionTema);
        System.out.println(VERDE + "Has elegido el tema: " + tema + RESET);

        // Solicitar dificultad (1 a 5)
        System.out.print(CYAN + "Selecciona dificultad (1-Fácil, 2-Media, 3-Difícil, 4-Experto, 5-Mortal): " + RESET);
        dificultad = entrada.nextInt();
        while (dificultad < 1 || dificultad > 5) {
            System.out.print(ROJO + "Valor inválido. Ingrese entre 1 y 5: " + RESET);
            dificultad = entrada.nextInt();
        }

        // Seleccionar palabra secreta
        palabraSecreta = seleccionarPalabra(palabras, opcionTema, dificultad);

        // Inicializar palabra adivinada con guiones bajos
        StringBuilder adivinada = new StringBuilder("_".repeat(palabraSecreta.length()));

        // --------- Bucle principal del juego ---------
        while (vidas > 0 && !adivinada.toString().equalsIgnoreCase(palabraSecreta)) {

            mostrarMuneco(errores);
            System.out.println("Palabra: " + MAGENTA + adivinada + RESET);
            System.out.println("Vidas restantes: " + VERDE + vidas + RESET);

            System.out.print("Letras usadas: ");
            for (String l : letrasUsadas) {
                if (!l.equals("")) System.out.print(l + " ");
            }
            System.out.println();

            // Leer letra del usuario
            System.out.print(CYAN + "Ingresa una letra: " + RESET);
            letra = entrada.next().toLowerCase();

            // Validar una sola letra
            if (letra.length() != 1 || !Character.isLetter(letra.charAt(0))) {
                System.out.println(ROJO + "Por favor, ingresa una única letra válida." + RESET);
                continue;
            }

            // Verificar si ya fue usada
            if (letraYaUsada(letra, letrasUsadas)) {
                System.out.println(AMARILLO + "Ya usaste esa letra." + RESET);
            } else {
                agregarLetraUsada(letra, letrasUsadas);

                // Buscar letra en palabra
                if (buscarLetraEnPalabra(letra, palabraSecreta, adivinada)) {
                    System.out.println(VERDE + "¡Correcto!" + RESET);
                } else {
                    System.out.println(ROJO + "Incorrecto." + RESET);
                    errores++;
                    vidas--;
                }
            }

            System.out.println("----------------------------");
        }

        // --------- Resultado final ---------
        if (adivinada.toString().equalsIgnoreCase(palabraSecreta)) {
            System.out.println(VERDE + "\n🎉 ¡Felicidades! Adivinaste la palabra: " + palabraSecreta + RESET);
        } else {
            mostrarMuneco(errores);
            System.out.println(ROJO + "\n💀 ¡Perdiste! La palabra era: " + palabraSecreta + RESET);
        }

        entrada.close();
    }
}
