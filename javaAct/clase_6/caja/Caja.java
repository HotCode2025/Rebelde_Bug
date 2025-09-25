
package caja;

public class Caja {
    // Atributos
    int ancho;
    int alto;
    int profundidad;

    // Constructor vacío
    public Caja() {
    }

    // Constructor con parámetros
    public Caja(int ancho, int alto, int profundidad) {
        this.ancho = ancho;
        this.alto = alto;
        this.profundidad = profundidad;
    }

    // Método para calcular volumen
    public int calcularVolumen() {
        return ancho * alto * profundidad;
    }
}
