/*
Ejercicio 7: ejercicio: Pedir números hasta que se introduzca uno negativo
y calcular la media. Clase Scanner
 */
package clase4;

import java.util.Scanner;

public class clase4ejercicio7clasescanner {
 
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numero;//en la variable número se guardan los valores
        int suma = 0;//en la variable suma la suma de todos los números
        int contador = 0;//cuanta los números que llevamos

        System.out.println("Introduce números, si deseas terminar ingresa un número negativo:");
        
        while (true) {//ciclo
            
            numero = sc.nextInt();//lee el número entero y lo guarda en la variable número
            
            if (numero < 0) {//si el número es negativo, salimos del ciclo con break
               break;
            }
            suma += numero;//la variable suma va sumando los números 
            contador++;//se suma uno al contador
            System.out.println("Introduce números, si deseas terminar ingresa un número negativo:");//colocamos este mje aquí para que lo muestre antes de ingresar cada número
        }

        if (contador > 0) {//condición para que al menos haya un número ingresado y evitar la divivión por cero
            double media = (double) suma / contador;//Calcula la media (promedio), double permite números decimales
            System.out.println("La media es: " + media);//muestra la media por pantalla
        } else {
            System.out.println("No se introdujeron números positivos");//para el caso en que no se introduzcan números positivos muestra mje
        }

    }
}  

