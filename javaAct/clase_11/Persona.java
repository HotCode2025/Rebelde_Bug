// //11.4 Arreglos Parte 4

package javaAct.clase_11;

/**
 * Clase Modelo que representa a una Persona.
 * Encapsula la información básica de una persona, en este caso, su nombre.
 */
public class Persona {
    
    // El 'private' asegura que el nombre no pueda ser modificado directamente
    // desde fuera de esta clase, protegiendo los datos.
    private String nombre;

    /**
     * Constructor para crear un nuevo objeto Persona.
     * @param nombre El nombre inicial de la persona.
     */
    public Persona(String nombre) {
        this.nombre = nombre;
    }

    /**
     * Obtiene el nombre de la persona.
     * @return El nombre actual de la persona.
     */
    public String getNombre() {
        return nombre;
    }

    /**
     * Establece o modifica el nombre de la persona.
     * @param nombre El nuevo nombre para la persona.
     */
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    /**
     * Sobrescribe el método toString() de la clase Object.
     * Esto permite que el objeto se imprima de forma legible
     * (por ejemplo, en un System.out.println).
     * @return Una representación en String del objeto Persona (su nombre).
     */
    @Override
    public String toString() {
        // Ahora, al imprimir un objeto Persona, se mostrará su nombre.
        return this.nombre;
    }
}