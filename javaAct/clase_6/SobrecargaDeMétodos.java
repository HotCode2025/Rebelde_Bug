
package clase_6;

public class SobrecargaDeMétodos {
    // atributos de la clase
    int a;
    int b;
    
    // el constructor es un metodo especial 
    public SobrecargaDeMétodos (){ // constructor 1
        System.out.println("Se esta ejecutando este constructor numero uno");
    }
    
    public SobrecargaDeMétodos (int a, int b) { // constructor 2
        this.a = a;
        this.b = b;
        System.out.println("se esta ejecutando este costructor dos");
    }
    
           
}
