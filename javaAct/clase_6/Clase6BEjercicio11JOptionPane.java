/*
JOPTIONPANE
Ejercicio 11: Diseñar un programa que muestre el producto
de los 10 primeros números impares
Hacerlo con JOptionPane 
 */
package EjerciciosClase6B;

import javax.swing.JOptionPane;

public class Ejercicio6BJoption {

    public static void main(String[] args) {

        int producto = 1;
        int cantidad = 0;

        while (cantidad < 10) {
            String input = JOptionPane.showInputDialog("Ingresa un número impar (" + (cantidad + 1) + "/10):");

            try {
                int numero = Integer.parseInt(input);

                if (numero % 2 != 0) {
                    producto *= numero;
                    cantidad++;
                } else {
                    JOptionPane.showMessageDialog(null, "Ese número es par. Por favor, ingresá un número impar.");
                }

            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(null, "Entrada inválida. Ingresá un número entero.");
            }
        }
        JOptionPane.showMessageDialog(null, "El producto de los 10 números impares ingresados es: " + producto);

    }
}