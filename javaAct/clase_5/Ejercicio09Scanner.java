
package clase5;


import java.util.Scanner;

public class Clase5Scanner {

    public static void main(String[] args) {
        /*
        CON Clase SCANNER
        
        Ejercicio 9: Pedir el día, mes y año de una fecha e
        indicar si la fecha es correcta. Suponiendo que
        todos los meses son de 30 días
        */

        boolean fechaCorrecta = false;

        while (!fechaCorrecta) {
            try {
                
                Scanner scanner = new Scanner(System.in);
                        
                System.out.println("Ingresa el año: ");
                int año = scanner.nextInt();
                System.out.println("Ingresa el mes (1-12): ");
                int mes = scanner.nextInt();
                System.out.println("Ingresa el día (1-30): ");
                int dia = scanner.nextInt();
                
                if (mes >= 1 && mes <= 12 && dia >= 1 && dia <= 30) {
                    fechaCorrecta = true;
                    System.out.println("La fecha ingresada es válida: " + dia + "/" + mes + "/" + año);
                } else {
                    System.out.println("Fecha inválida. Recordá que todos los meses tienen 30 días.");
                }
            } catch (NumberFormatException e) {
                System.out.println( "Entrada inválida. Por favor, ingresá solo números.");
            }
        }
    }
} 