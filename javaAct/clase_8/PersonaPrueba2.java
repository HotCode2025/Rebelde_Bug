//Contexto Estatico Practica 2 
package test;

import domain.Persona;
public class PersonaPrueba2 {
    private int contador;
    public static void main(String[] args) {
        Persona persona1 = new Persona("Ariel");
        System.out.println("persona1 = " + persona1);
        Persona persona2 = new Persona("Micaela");
        System.out.println("persona2 = " + persona2);
        imprimir(persona1);
        imprimir(persona2);
        //this.contador = 10;//No se puede refenciar desde un contexto estático
        PersonaPrueba personaP1 = new PersonaPrueba();
        System.out.println(personaP1.getContador());
    }
    
  
    //Hasta aquí Contexto Estático Practica 2 Ejecutar con Debug File
    
    
    //Desde aquí en adelante, es el ejercicio 
    public static void imprimir(Persona persona){
        System.out.println("persona = " + persona);
    }
    public int getContador(){
        imprimir (new Persona("Micaela"));
        return this.contador;
        
    }
}

