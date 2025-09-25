/* Scanner
 Ejercicio 12: Pedir un número y calcular su factorial
Hacerlo con clase Scanner.
 */
package clase6;

import java.util.Scanner;


public class Clase6Ejercicio12Scanner {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.print("Ingrese un número para calcular su factorial: ");
        int numero = entrada.nextInt();

        long factorial = 1;
            for (int i = 1; i <= numero; i++) {
            factorial *= i;
        }

        System.out.println("El factorial de " + numero + " es: " + factorial);
        entrada.close();
    }
}
