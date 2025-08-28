
package clase3ejercicioconciclos3;

import javax.swing.JOptionPane;
public class Clase3EjerciciosConCiclos3JOpcionP{
        public static void main(String[] args) {
         
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));//Aquí se ingrea el númro
        while (numero != 0) { // Mientras sea distinto de cero hacer
            if (numero % 2 == 0) {//Si el módulo de dos da resto cero (es par)
                JOptionPane.showMessageDialog(null, numero + " es PAR.");//se imprime por pantalla
            } else {//sino
                JOptionPane.showMessageDialog(null, numero + " es IMPAR.");
            }

            numero = Integer.parseInt(
                JOptionPane.showInputDialog("Digite un número (0 para salir):")//Pedimos otra vez ingresar el número
            );
        }

        JOptionPane.showMessageDialog(null, "El programa finaliza con cero");//Cuando se ingresa 0 finaliza 
    }  
}

