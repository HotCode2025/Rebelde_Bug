
package clase_6;

public class PasoPorValor {
    public static void main(String[] args) {
        
        var valorx = 20;
        System.out.println("valorx =" + valorx);
        cambioValor(valorx); 
    }
    
    public static void cambioValor (int arg1){
        System.out.println("argq = " + arg1);
        arg1 = 15;
    }

}
