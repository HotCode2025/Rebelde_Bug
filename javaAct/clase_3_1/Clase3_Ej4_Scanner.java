/*
Ejercicio 4: Pedir numeros hasta que se teclee uno negativo y mostrar cuantos numeros se han introducido.
Lo hacemos primero con scanner 
Luego con la clase JOptionPane
*/

import java.util.Scanner;

public class Ciclos04 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numero;
        int contador = 0;
        System.out.println("Ingrese cualquier numero:");
        do {
            numero = sc.nextInt();
            if (numero >= 0) {
                contador++;
            }
        } while (numero >= 0);

        System.out.println("Se introdujeron " +contador+ " números.");
    }
}