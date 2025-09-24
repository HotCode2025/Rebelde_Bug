
import javax.swing.JOptionPane;

public class Ejercicio12CiclosJOptionPane {
     public static void main(String[] args) {
        String input = JOptionPane.showInputDialog("Ingrese un número entero: ");
        int numero = Integer.parseInt(input);
        long factorial = 1;
        for (int i =1; i <= numero;i++){
            factorial *= i;
        }
        JOptionPane.showMessageDialog(null, "El factorial de " +numero+ " es " +factorial);
        
        
    }
    
}


