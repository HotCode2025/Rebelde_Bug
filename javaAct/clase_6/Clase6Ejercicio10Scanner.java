/* Scanner
Ejercicio 10: Pedir 10 números y escribir la suma total
Hacerlo con la Clase Scanner

*/
package clase6;
import java.util.Scanner;

public class Clase6Ejercicio10Scanner {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int suma = 0;

        // Pedir 10 números
        for (int i = 1; i <= 10; i++) {
            System.out.print("Ingrese el número " + i + ": ");
            int numero = entrada.nextInt();
            suma += numero;
        }

        // Mostrar el resultado
        System.out.println("La suma total de los 10 números es: " + suma);

        entrada.close();
    }
}