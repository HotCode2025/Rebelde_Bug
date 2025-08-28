package javaa.clase_3.parte_1;

import javax.swing.JOptionPane;

public class ejercicio_4_JOptionPane {
    public static void main(String[] args) {
        int numero;
        int contador = 0;

        do {
            // Pedimos número con ventana emergente
            String input = JOptionPane.showInputDialog("Ingrese un número (negativo para salir):");
            numero = Integer.parseInt(input); // Convertimos el texto a entero

            if (numero >= 0) {
                contador++; // si no es negativo, lo contamos
            }

        } while (numero >= 0); // se repite hasta que sea negativo

        // Mostramos el resultado
        JOptionPane.showMessageDialog(null, "Se introdujeron " + contador + " números.");
    }
}
