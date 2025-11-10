/*
En este ejercicio no usamos la clase SCANNER
Ejercicio 1: Leer un número y mostrar su cuadrado, repetir
el proceso hasta que se introduzca un número negativo
*/

package Clase2Ejercicio1SinScanner;
import javax.swing.JOptionPane;
public class Clase2Ejercicio1SinScanner {
    public static void main(String[] args) {
        int numero, cuadrado;
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número"));//la clase JOptionPane trabaja con String por eso cdo la usemos 
        //acá vamos a tener que hacer una conversión Integer
        while(numero>=0){//Mientras el número sea igual a cero o positivo
            cuadrado=(int)Math.pow(numero,2);
            System.out.println("El numero "+numero+" elevado al cuadrado es: "+cuadrado);
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número"));;
                    
            }
        System.out.println("El programa ha finalizado por número negativo");
    
    }
}
