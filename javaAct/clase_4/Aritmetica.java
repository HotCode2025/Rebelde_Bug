
package Operaciones;

public class Aritmetica {
    
    //atributos de la clase
    int a;
    int b;
    //Metodo
    public void sumarNumeros(){
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
            
    }
    public static void main(String[] args) {
        Aritmetica aritmetica = new Aritmetica();
        aritmetica.a = 5;
        aritmetica.b = 3;
        aritmetica.sumarNumeros();
    }
}
