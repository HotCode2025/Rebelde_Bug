
package clase6;

import javax.swing.JOptionPane;

public class Clase6Ejercicio10JOptionPane {
    public static void main(String[] args) {
        int suma = 0;

        // Pedir 10 números
        for (int i = 1; i <= 10; i++) {
            int numero = Integer.parseInt(
                JOptionPane.showInputDialog("Ingrese el número " + i + ":")
            );
            suma += numero;
        }

        // Mostrar el resultado
        JOptionPane.showMessageDialog(null, "La suma total de los 10 números es: " + suma);
    }
}
