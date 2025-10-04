
package clase_6;

public class prueba {
 public static void main(String[] args) {
        
        var a = 10; // variable local
        int b = 6; // memoria stack
     
        miMetodo(); // llmamatos el metodo nuevo
        // Llamando al constructor 1 (sin parámetros)
        SobrecargaDeMétodos obj1 = new SobrecargaDeMétodos();
        
        // Llamando al constructor 2 (con parámetros)
        SobrecargaDeMétodos obj2 = new SobrecargaDeMétodos(10, 20);
        
        // Mostramos los valores de a y b cargados con el constructor 2
        System.out.println("Valores de obj2: a = " + obj2.a + ", b = " + obj2.b);
    }
 
    public static void miMetodo (){
       // a = 10; // una variable esta limitada
        System.out.println("aqui hay otro metodo ");
      
        // prueba = null; nunca se debe utilizar
        // System.gc(); metodo para limpiar residuos, es pesado, no se utiliza 
    }
 
}