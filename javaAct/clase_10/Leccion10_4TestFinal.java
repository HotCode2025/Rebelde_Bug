/*
    Uso de la palabra Final
Esta palabra tiene diferentes significados
dependiendo donde se aplique:
        Variables: Evita cambiar el valor que almacena la variable 
        Métodos: Evita que se modifique la definición o el comportamiento
│           de un método desde una subclase (hija)
        Clases: Evita que se creen clases hijas
Otra caracteristica es que normalmente, cuando trabajamos con variables 
se combina con el modificador de acceso estático para convertir una 
variable en una constante, es decir que no se puede modificar su valor, 
el ejemplo de esto es la clase Math en la cuál todos sus atributos son 
de tipo static y final, es por esto que la variable pi* se conoce como 
una constante.
*/
package test;

import domain.Leccion10_4Persona;

public class Leccion10_4TestFinal {
    public static void main(String[] args) {
        final int miDni = 12111098;
        System.out.println("miDni = " + miDni);
        //miDni = 55791376; NO se puede modificar
        //Persona.CONSTANTE_AQUI = 99; //No se modifica
        System.out.println("Mi atributo constante es: = " + Leccion10_4Persona.CONSTANTE_AQUI);
        
        final Leccion10_4Persona persona1 = new Leccion10_4Persona();
        //persona1 = new Leccion10_4Persona(); No se puede asignar una nueva referencia
        persona1.setNombre("Rebelde Bug");
        System.out.println("persona1 nombre = " + persona1.getNombre());
        persona1.setNombre("Bug Rebelde");
        System.out.println("persona1 nombre = " + persona1.getNombre());
        
    }
}