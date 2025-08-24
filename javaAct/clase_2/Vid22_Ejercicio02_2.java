
import javax.swing.JOptionPane;
/*
Ejercicio 2: Leer un numero e indicar si es positivo o negativo. El proceso se repetira hastga que se introduzca un cero 0
*/
/*EJERCICIO JOptionPane*/
public class Vid22_Ejercicio02_2 {
    public static void main(String[] args) {
        var numero =Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: ")) ;
        while(numero !=0 ){
            if(numero > 0){
                JOptionPane.showMessageDialog(null, "El numero "+numero+" es POSITIVO");
            }
            else{
                JOptionPane.showMessageDialog(null, "El numero "+numero+" es NEGATIVO");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero"));
        }
        JOptionPane.showMessageDialog(null, "El numero "+numero+"finaliza el programa");
    }
}
