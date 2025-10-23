package Operaciones;

//CLASES: [5.1];[5.2];[5.3];[5.4];[5.5]

public class Aritmetica {  
    //Atributos de la clase
    int a;
    int b;
    
    //Método
    public void sumarNumeros() {
       int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }
    
    public int sumarConRetorno(){
        //int resultado = a + b;
        return this.a + this.b;
    }
    
    public int sumarConArgumentos(int arg1, int arg2){
        this.a = arg1; //El argumento a se asigna al atributo this.a
        this.b = arg2; 
        //return a + b;
        return this.sumarConRetorno(); 
    }
}