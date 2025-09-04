/*
Ejercicio 6: Pedir numeros hata que se teclee un 0, mostrar la suma de todos los numeros introducidos.
*/
package Ciclos06;

import javax.swing.JOptionPane;

public class Clase4Ejercicio6 {
    public static void main(String[] args) {
        int numero;
        int suma = 0;

        do {
            numero = Integer.parseInt(JOptionPane.showInputDialog("Introduce un número (0 para salir):"));
            suma += numero;
        } while (numero != 0);

        JOptionPane.showMessageDialog(null, "La suma de todos los números introducidos es: " + suma);
    }
}