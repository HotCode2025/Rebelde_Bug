// 📦 Paquete: define en qué "carpeta lógica" está la clase
// Debe coincidir con la estructura de carpetas en tu proyecto
package javaa.clase_2;

// 📥 Importamos la clase Scanner para poder leer datos del teclado
import java.util.Scanner;

// 👨‍💻 Declaramos la clase principal (debe llamarse igual que el archivo .java)
public class ejercicio_1 {
    
    // 🔑 Método principal: es el punto de entrada del programa
    public static void main(String[] args) {
        
        // ✏️ Creamos un objeto Scanner para leer datos desde la consola
        Scanner sc = new Scanner(System.in);

        // 📌 Variable donde vamos a guardar el número ingresado
        int numero;

        // 👀 Pedimos el primer número al usuario
        System.out.println("Introduce un número (negativo para salir): ");
        numero = sc.nextInt(); // 👉 Leemos el número por teclado

        // 🔁 Bucle while: se repite mientras el número sea mayor o igual a 0
        while (numero >= 0) {
            // 🧮 Calculamos el cuadrado del número
            int cuadrado = numero * numero;

            // 📢 Mostramos el resultado
            System.out.println("El cuadrado de " + numero + " es: " + cuadrado);

            // 👀 Pedimos otro número
            System.out.println("Introduce otro número (negativo para salir): ");
            numero = sc.nextInt(); // 👉 Volvemos a leer
        }

        // 🚪 Si llegamos acá es porque se ingresó un número negativo
        System.out.println("Programa finalizado.");

        // 🧹 Cerramos el Scanner (buena práctica para liberar recursos)
        sc.close();
    }
}