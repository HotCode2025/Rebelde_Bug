//Utilizando CLASE JOptionPane

/*
Ejercicio 5: Realizar un juego para adivinar un número, para ello generar un número 
aleatorio entre 0-100, y luego ir pidiendo números indicando "es mayor" o
"es menor" según sea mayor o menor con respecto a N El proceso termina cuando el
 usuario acierta y mostramos el número de intentos hechos. 
 */

import javax.swing.JOptionPane;

public class Ejercicio5JOptionPane {
    
   public static void main(String[] args) {
        int numAleatorio = (int)(Math.random() * 101); // Número entre 0 y 100
        int intentos = 0;
        int numIngresado = -1;

        while (numIngresado != numAleatorio) {
            String entrada = JOptionPane.showInputDialog(null, "Ingresa un número entre 0 y 100:");
            
            if (entrada == null) {
                JOptionPane.showMessageDialog(null, "Juego cancelado.");
                return;
            }
            try {
                numIngresado = Integer.parseInt(entrada);
                intentos++;

                if (numIngresado < numAleatorio) {
                    JOptionPane.showMessageDialog(null, "El número ingresado es menor que el número a adivinar.");
                } else if (numIngresado > numAleatorio) {
                    JOptionPane.showMessageDialog(null, "El número ingresado es mayor que el número a adivinar.");
                } else {
                    JOptionPane.showMessageDialog(null, "Felicidades, Adivinaste el número en " + intentos +" intento/s.");
                }

            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(null, "Por favor, ingresa un número válido.");
            }
        }
    }
}
