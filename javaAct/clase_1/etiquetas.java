public class etiquetas {
    public static void main(String[] args) {
         //Etiquetas (Labels)
        inicio:
        for(int i = 0; i < 10; i++){
            if (i % 2 == 0) {
                System.out.println("conteo = " + i);
                break inicio;
            }
        }
    }
}
