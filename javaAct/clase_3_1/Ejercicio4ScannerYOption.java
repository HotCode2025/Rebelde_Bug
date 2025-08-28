//Ejercicio4: Pedir números hasta que se teclee uno negativo
//y mostrar cuántos numeros se han introducido
//Lo hacemos primero con Scanner y luego con JOptionPane
package Clase03;

import javax.swing.JOptionPane;

public class Ejercicio4ScannerYOption {
    public static void main(String[] args) {
        int numero;
        int contador =0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while (numero >= 0){
            contador++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        }
        JOptionPane.showMessageDialog(null, "Se introdujeron " + contador + " numeros");
        
    }
}
