package caja;

public class PruebaCaja {
    public static void main(String[] args) {
        
        // Uso del constructor vacío
        Caja caja1 = new Caja();
        caja1.ancho = 3;
        caja1.alto = 2;
        caja1.profundidad = 6;

        System.out.println("Volumen de caja1 = " + caja1.calcularVolumen());

        // Uso del constructor con parámetros
        Caja caja2 = new Caja(4, 5, 6);
        System.out.println("Volumen de caja2 = " + caja2.calcularVolumen());
    }
}