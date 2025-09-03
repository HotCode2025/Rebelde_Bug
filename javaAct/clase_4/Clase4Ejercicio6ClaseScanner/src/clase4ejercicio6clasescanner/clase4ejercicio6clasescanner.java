
package clase4ejercicio6clasescanner;

import java.util.Scanner;

public class clase4ejercicio6clasescanner {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);//leemos lo que ingresa el usuario
        int numero;//número guardará los números ingresados
        int suma = 0;//suma se inicializaa en cero

        do {
            System.out.print("Introduce un número, si deseas terminar presiona 0 (cero): ");//muestra mje por pantalla
            numero = entrada.nextInt();//leemos el número ingresado por el usuario
            suma += numero;//a la variable suma se le adiciona el número ingresado
        } while (numero != 0);//el ciclo se repite mientras el número ingresado sea distinto de 0

        System.out.println("La suma de los números introducidos es: " + suma);//mje por pantalla la suma de todos los números ingresados
    }
}

