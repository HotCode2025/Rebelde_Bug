
package clase4;

public class PruebaPersona {
    public static void main(String[] args) {//método main se usa para ejecutar el programa
        //creamos el objeto persona1
        Persona persona1;
        persona1= new Persona();//llamamos al constructor cuando ponemos Persona()
        persona1.nombre = "Ivana";//el valor hexadecimal normalmente comienza con 0x, este vlor es una referencia en memoria yse le asigna a la variable persona1
        persona1.apellido = "Molina";//le asignamos valor al atributo apellido
        persona1.obtenerInformacion();//acá llamamos al método, lo que hace es mostrar la información de los atributos en la clase, como los acabamos de modificar va a mostrar Ivana Molina
        //cdo la variable persona1 se está asociando al constructor de la clase persona esa variable persona1 pasa a ser un OBJETO
        //el constructor nos permite asignarle valores al objeto desde que lo creamos
        //una variable se almacena en espacios diferentes a los objetos en la memoria y java los administra de manera distinta
        //el constructor es un método especial que reserva memoria para poder CREAR OBJETOS
        //Cdo crea el objeto el constructor devuelve la referencia de donde se creó el objeto y se lo asigna a la variable 
        //una vez hecha esta conexión se puede acceder a los atributos y métodos de la clase, en este caso la clase persona 
        Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2);
        System.out.println("persona1 = " + persona1);
        persona2.obtenerInformacion();
        persona2.nombre= "Ariel";
        persona2.apellido= "Betancud";
        persona2.obtenerInformacion();
        Persona persona3 = new Persona();
        persona3.nombre = "Osvaldo";
        persona3.apellido = "Giordanini";
        System.out.println("persona3 = " + persona3);
        persona3.obtenerInformacion();
        
    }
}
