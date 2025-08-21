
public class Ciclo_Do_While {
    public static void main(String[] args) {
    
    //Ciclo DO WHILE
        var contador = 0;
        do{
           System.out.println("contador = " + contador);
           contador++;
        }while(contador <= 7); //Primero se ejecuta el código DO y luego la condición WHILE. Siempre se ejecuta al menos 1 vez
    }
}