//6.6 POO: Paso por referencia
//6.7 Palabras return y null
package clase_6;

import javaa.clase_4.Personaa;

public class PasoPorReferencia {
    public static void main(String[] args) {
        Personaa persona1 = new Personaa();
        persona1.nombre = "carlos";
        System.out.println("persona1 nombre =" + persona1.nombre);
        cambiarValor(persona1);   
        System.out.println("El cambio que hacemos es: " + persona1);
        System.out.println("El cambio que hacemos es: " + persona1.nombre);
        persona1 = cambiarElvalor(persona1);
        Personaa persona2 = null;
        persona2 = cambiarElvalor(persona2);
        System.out.println("el valor nuevo es: " + persona2.nombre);
    }
    
    
    public static void cambiarValor(Personaa persona){ // paso por rederencia
        persona.nombre = "maria";
    }
    
    public static Personaa cambiarElvalor(Personaa persona){
        if (persona == null){
            System.out.println("vallor de persona es : NULL");
            return null;
        }
        else {
            
         persona.nombre = "pepe";
        return persona;
        }

    }
}
