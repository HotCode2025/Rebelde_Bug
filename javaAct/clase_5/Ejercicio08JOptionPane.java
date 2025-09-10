
package Ejercicios_clase5;

import javax.swing.JOptionPane;

public class Ejercicio08JOptionPane {
    public static void main(String[] args) {
        int N = Integer.parseInt(JOptionPane.showInputDialog("Ingresa un número N:"));

        StringBuilder resultado = new StringBuilder("Números del 1 al " + N + ":\n");
        for (int i = 1; i <= N; i++) {
            resultado.append(i).append("\n");
        }

        JOptionPane.showMessageDialog(null, resultado.toString());
    }
}