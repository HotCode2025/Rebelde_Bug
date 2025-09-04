/*Ejercicio 7: Pedir números hasta que se introduzca uno negativo y calcular la media*/

import javax.swing.JOptionPane;
public class Ejercicio7JOptionPane {
     public static void main(String[] args) {
        int suma = 0;
        int contador = 0;
        int numero;
        
        while (true){
            String input = JOptionPane.showInputDialog("Introduce un numero (negativo para terminar):");
            if (input == null){
                JOptionPane.showMessageDialog(null, "Operacion cancelada. ");
                return;
            }
            try {
                numero = Integer.parseInt(input);
                if (numero < 0){
                    break;
                }
                suma += numero;
                contador++;
            } catch(NumberFormatException e){
                JOptionPane.showMessageDialog(null, "Entrada invalida, por favor introduce un numero entero ");
            }

        }
        if (contador > 0){
            double media = (double)suma / contador;
            JOptionPane.showMessageDialog(null, "La media de los numeros introducidos es: " + media);
        } else {
            JOptionPane.showMessageDialog(null, "No se introdujeron numeros validos ");
        }
    
}
     }

