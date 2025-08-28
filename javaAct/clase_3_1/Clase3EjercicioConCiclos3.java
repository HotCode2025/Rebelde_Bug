/*Ejercicio 3: Leer un números hsata que se introduzca un cero
Para cada uno indicar si es par o impar.
Primero lo haremos con la clase Scanner
Luego con la clase JOptionPame*/

// clase scanner
package clase3ejercicioconciclos3;

import java.util.Scanner;

public class Clase3EjercicioConCiclos3 {
 
    public static void main(String[] args) {
     Scanner entrada = new Scanner(System.in);
        int numero;
        System.out.println("Digite un numero: ");//pedimos un número por pantalla
        numero = Integer.parseInt(entrada.nextLine());//se lo asignamos a la variabel número 
        while(numero!=0){//Mientras el número sea distinto de cero
           if (numero % 2 == 0) {//si el resto del modulo de 2 da cero (par)
                    System.out.println(numero + " es PAR.");
                } else {
                    System.out.println(numero + " es IMPAR.");
                }
        System.out.println("Digite un numero: ");//pedimos otro número
        numero = Integer.parseInt(entrada.nextLine());
        }
     System.out.println("El programa finaliza con cero");//Si se ingresa cero mostramos mje por pantalla      
    }  
   
}

