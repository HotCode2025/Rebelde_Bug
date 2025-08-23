
package BreakContinue;

public class EjercicioBreakContinue04 {
    public static void main(String[] args) {
        for(var contando=0;contando<7;contando++){
            if(contando%2==0){
            System.out.println("contando = " + contando);
            //break;//rompe el ciclo y sale en este caso sólo va a imprimir el cero que es el primer número par que encuentra  yluego sale
            }
        }
        for(var contando=0;contando<7;contando++){
            if(contando%2!=0){//si es número impar
                continue;//vamos a la sgte iteración continúa con el ciclo sin imprimir
            }
            System.out.println("contando = " + contando);
        }
    }
}