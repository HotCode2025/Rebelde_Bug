// 8.1 Palabra static con métodos: Parte 1 y 2
// 8.2 Atributos estáticos
// 8.3 Atributos estáticos vs No estáticos
// 8.4 Uso de la palabra static: Parte 1 y 2
// 8.5 Creación de constantes estáticas
class Persona {
  static contadorPersonas = 0;           // Atributo estático (compartido por la clase)

  static get MAX_OBJ() {                 // "Constante" estática (solo lectura mediante getter)
    return 5;
  }

  constructor(nombre, apellido) {
    if (Persona.contadorPersonas >= Persona.MAX_OBJ) {
      console.log('Se ha superado el máximo de objetos permitidos');
      // Opcional: lanzar un error o asignar un id nulo
      this.idPersona = null;
      this.nombre = nombre;
      this.apellido = apellido;
      return; // Salimos sin incrementar
    }

    this.nombre = nombre;                // Atributos de instancia (no estáticos)
    this.apellido = apellido;
    this.idPersona = ++Persona.contadorPersonas; // Incremento ÚNICO y asignación
  }

  // Método estático: se invoca desde la clase, no desde la instancia
  static saludar() {
    console.log('Saludos desde el método static');
  }

  // Método de instancia (no estático)
  nombreCompleto() {
    // Si idPersona es null (por superar MAX_OBJ), lo reflejamos
    const id = (this.idPersona ?? '—');
    return `${id} ${this.nombre} ${this.apellido}`;
  }

  // Método estático que recibe una INSTANCIA y la usa
  static saludar2(persona) {
    if (persona instanceof Persona) {
      console.log(`${persona.nombre} ${persona.apellido}`);
    } else {
      console.log('Debes pasar una instancia de Persona');
    }
  }
}

// ---- Pruebas ----
let persona1 = new Persona('Pepe', 'Gómez');
Persona.saludar();            // OK
Persona.saludar2(persona1);   // Pepe Gómez

console.log(Persona.contadorPersonas); // 1
console.log(persona1.nombreCompleto()); // "1 Pepe Gómez"

// MAX_OBJ es estático y de solo lectura (getter)
console.log(Persona.MAX_OBJ); // 5
// Persona.MAX_OBJ = 10; // No tendrá efecto: no hay setter

// Creamos más instancias hasta el límite
let persona2 = new Persona('Karla', 'López');
let persona3 = new Persona('Ana', 'Pérez');
let persona4 = new Persona('Luis', 'Martínez');
let persona5 = new Persona('Marta', 'Ruiz');
console.log(Persona.contadorPersonas); // 5

// Supera el límite (muestra el mensaje y no incrementa)
let persona6 = new Persona('Extra', 'FueraDeLimite');
console.log(Persona.contadorPersonas); // sigue en 5
console.log(persona6.nombreCompleto()); // "— Extra FueraDeLimite"


