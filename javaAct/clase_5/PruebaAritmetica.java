package Operaciones;

//CLASES: [5.1];[5.2];[5.3];[5.4];[5.5]

public class PruebaAritmetica {
    
    public static void main(String[] args) {

        Aritmetica aritmetica5 = new Aritmetica();
        aritmetica5.a = 1;
        aritmetica5.b = 8;
        aritmetica5.sumarNumeros();

        int resultado = aritmetica5.sumarConRetorno();
        System.out.println("resultado = " + resultado);
        
        resultado = aritmetica5.sumarConArgumentos(66,99);
        System.out.println("Resultado usando argumentos= "+ resultado);
    }
}