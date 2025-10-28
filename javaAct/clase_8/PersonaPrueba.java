package test;

import dominio.Persona;
public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo", 57.000, false);
        System.out.println("persona1 su nombre es: "+persona1.getNombre());
        //Modificar a traves de los metodos
        persona1.setNombre("Juan Ignacio");
        //persona1.nombre = "Juan Ignacio"; //Ya no se puede utilizar
        //System.out.println("Nombre es: "+persona1.nombre);//Error
        System.out.println("persona1 con su nombre modificado: "+persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: "+persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: "+persona1.isEliminado());
        
        //Tarea= crear otro objeto de tipo persona, asignar valores de manera inicial
        //e imprimir, luego modificar sus valores y luego volver a imprimir
        
        Persona persona2 = new Persona("Micaela", 90.000, false);
        System.out.println("persona 2 su nombre es: "+persona2.getNombre());
        System.out.println("persona 2 el resultado para el sueldo: "+persona2.getSueldo());
        System.out.println("persona2 para obtener el booleano: "+persona2.isEliminado());
        
        //Modificamos valores de persona2
        persona2.setNombre("Melany");
        persona2.setSueldo(94.000);
        persona2.setEliminado(true);
        
        System.out.println("persona2 con su nombre modificado: "+persona2.getNombre());
        System.out.println("persona2 el resultado para el sueldo: "+persona2.getSueldo());
        System.out.println("persona2 para obtener eel booleano: "+persona2.isEliminado());
        
        
    }
    
}
