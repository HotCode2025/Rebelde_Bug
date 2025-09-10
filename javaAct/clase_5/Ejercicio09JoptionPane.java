import javax.swing.JOptionPane;

/*Ejercicio 9: Pedir el día, mes y año de una fecha e indicar si la fecha es correcta. Suponiendo
que todos los meses son de 30 dias (Con JOptionPane)*/

public class FechaJOptionPane {
    public static void main(String[] args) {
        int dia = Integer.parseInt(JOptionPane.showInputDialog("Introduce el día:"));
        int mes = Integer.parseInt(JOptionPane.showInputDialog("Introduce el mes:"));
        int anio = Integer.parseInt(JOptionPane.showInputDialog("Introduce el año:"));

        if (dia >= 1 && dia <= 30 && mes >= 1 && mes <= 12 && anio > 0) {
            JOptionPane.showMessageDialog(null, "La fecha " + dia + "/" + mes + "/" + anio + " es correcta.");
        } else {
            JOptionPane.showMessageDialog(null, "La fecha no es correcta.");
        }
    }
}
