package domain;

public class Leccion10_4Persona {
    public final static int CONSTANTE_AQUI = 22;
    private String nombre;

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
       
    public void imprimir(){
        System.out.println("Método para imprimir");
    }
}