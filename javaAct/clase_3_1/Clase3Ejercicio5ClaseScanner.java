//Utilizando CLASE SCANNER

/*
Ejercicio 5: Realizar un juego para adivinar un número, para ello generar un número 
aleatorio entre 0-100, y luego ir pidiendo números indicando "es mayor" o
"es menor" según sea mayor o menor con respecto a N El proceso termina cuando el
 usuario acierta y mostramos el número de intentos hechos. 
 */

import java.util.Scanner;

public class Ejercicio5 {

    public static void main(String[] args) {
        //MENU
        System.out.println("***ADIVINA EL NÚMERO***");
        //Generar núm aleatorio
        int numAleatorio = (int) (Math.random() * 101);
        Scanner scanner = new Scanner(System.in);

        int intentos = 0;
        int numIngresado;

        do {
            System.out.println("Ingresa un número entre 0 y 100: ");
            numIngresado = scanner.nextInt();
            intentos++;

            if (numAleatorio > numIngresado) {
                System.out.println("El número ingresado es menor que el número a adivinar.");
            } else if (numAleatorio < numIngresado) {
                System.out.println("El número ingresado es mayor que el número a adivinar.");
            } else{
                System.out.println("Felicidades, Adivinó el número en " + intentos + " intento/s.");
            } 
        } while (numIngresado != numAleatorio);
        
        scanner.close();

    }
}