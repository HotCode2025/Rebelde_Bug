package clase_9;

import java.util.Date;

public class Persona {

    private String nombre;
    private char genero;
    private int edad;
    private String direccion;

    // Getters y Setters
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public char getGenero() {
        return genero;
    }

    public void setGenero(char genero) {
        this.genero = genero;
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public String getDireccion() {
        return direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }

    // Mostramos la información

    public String toString() {
        return "Nombre: " + nombre +
               ", Género: " + genero +
               ", Edad: " + edad +
               ", Dirección: " + direccion;
    }
}

//Se crea la clase Empleado que hereda de Persona

class Empleado extends Persona {
    // Atributos
    private int idEmpleado;
    private double sueldo;

    // Getters y Setters
    public int getIdEmpleado() {
        return idEmpleado;
    }

    public void setIdEmpleado(int idEmpleado) {
        this.idEmpleado = idEmpleado;
    }

    public double getSueldo() {
        return sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    // Mostrar datos

    public String toString() {
        return super.toString() +
               ", ID Empleado: " + idEmpleado +
               ", Sueldo: " + sueldo;
    }
}

// Se crea la clase Cliente que también hereda de Persona

class Cliente extends Persona {
    // Atributos
    private int idCliente;
    private Date fechaRegistro;
    private boolean vip;

    // Getters y Setters
    public int getIdCliente() {
        return idCliente;
    }

    public void setIdCliente(int idCliente) {
        this.idCliente = idCliente;
    }

    public Date getFechaRegistro() {
        return fechaRegistro;
    }

    public void setFechaRegistro(Date fechaRegistro) {
        this.fechaRegistro = fechaRegistro;
    }

    public boolean isVip() {
        return vip;
    }

    public void setVip(boolean vip) {
        this.vip = vip;
    }

    // Mostrar datos
    public String toString() {
        return super.toString() +
               ", ID Cliente: " + idCliente +
               ", Fecha Registro: " + fechaRegistro +
               ", VIP: " + vip;
    }


public class Main {
    public static void main(String[] args) {

        // Ahora creamos y probamos un Empleado
        Empleado empleado = new Empleado();
        empleado.setNombre("Carlos");
        empleado.setGenero('M');
        empleado.setEdad(30);
        empleado.setDireccion("Calle Falsa 123");
        empleado.setIdEmpleado(1);
        empleado.setSueldo(50000.0);

        System.out.println("=== Empleado ===");
        System.out.println(empleado);

        // Creamos y probamos un Cliente
        Cliente cliente = new Cliente();
        cliente.setNombre("Lucía");
        cliente.setGenero('F');
        cliente.setEdad(25);
        cliente.setDireccion("Av. Siempre Viva 742");
        cliente.setIdCliente(101);
        cliente.setFechaRegistro(new Date());
        cliente.setVip(true);

        System.out.println("\n *** Cliente ***");
        System.out.println(cliente);
    }
}

}
