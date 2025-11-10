
package EtiquetasLabels;

public class EjercicioLabels05 {
    public static void main(String[] args) {
        //uso de las palabras break y continue junto a las etiquetas (labels)
        inicio: //etiqueta
        for(var contando=0;contando<7;contando++){
            if(contando%2==0){
            System.out.println("contando = " + contando);
            break inicio;//nos manda a la etiqueta inicio
            }
        }
        start:
        for(var contando=0;contando<7;contando++){
            if(contando%2!=0){//si es número impar
                continue start;//lo envia a la etiquta start
            }
            System.out.println("contando = " + contando);
        }
    }
}
