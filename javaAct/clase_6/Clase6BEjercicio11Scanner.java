
/*
SCANNER
Ejercicio 11: Diseñar un programa que muestre el producto
de los 10 primeros números impares
Hacerlo con JOptionPane 
 */
package EjerciciosClase6B;

import java.util.Scanner;

public class ejercicio6BScanner {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int producto = 1;
        int cantidad = 0;

        while (cantidad < 10) {
            System.out.print("Ingresa un número impar (" + (cantidad + 1) + "/10): ");
            
            if (scanner.hasNextInt()) {
                int numero = scanner.nextInt();

                if (numero % 2 != 0) {
                    producto *= numero;
                    cantidad++;
                } else {
                    System.out.println("Ese número es par. Por favor, ingresá un número impar.");
                }
            } else {
                System.out.println("Entrada inválida. Ingresá un número entero.");
                scanner.next(); // limpiar entrada
            }
        }

        System.out.println("El producto de los 10 números impares ingresados es: " + producto);
    }
}