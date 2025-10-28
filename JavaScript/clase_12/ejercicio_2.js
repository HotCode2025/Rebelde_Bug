/*
  Crea un gestor de tareas simple que permite:
  Agregar tareas con un id y descripción.
  Marcar tareas como completadas.
  Listar todas las tareas con su estado.
 */
function createTaskManager() {
  // Arreglo privado que almacena las tareas
  let tasks = [];

  return {
    
     // Agrega una nueva tarea al arreglo.
    addTask: function(task) {
      const newTask = {
        id: tasks.length + 1,   // ID único (simple)
        description: task,      // Texto de la tarea
        completed: false        // Estado inicial
      };
      tasks.push(newTask);
      console.log(`Tarea agregada: "${task}"`);
    },

    
     //Marca una tarea como completada según su ID.

    completeTask: function(taskId) {
      const task = tasks.find(t => t.id === taskId);
      if (task) {
        task.completed = true;
        console.log(`Tarea completada: "${task.description}"`);
      } else {
        console.log(`No se encontró la tarea con ID ${taskId}`);
      }
    },

    
     // Muestra la lista de tareas con su estado.
   
    listTasks: function() {
      console.log("📋 Lista de tareas:");
      tasks.forEach(t => {
        const status = t.completed ? "✅ Completada" : "⏳ Pendiente";
        console.log(`${t.id}. ${t.description} - ${status}`);
      });
    }
  };
}

// Uso del gestor de tareas:
const myTasks = createTaskManager();
myTasks.addTask("Aprender JavaScript");
myTasks.addTask("Hacer ejercicio");
myTasks.listTasks();         // Muestra todas las tareas
myTasks.completeTask(1);     // Marca la primera como completada
myTasks.listTasks();         // Muestra la lista actualizada
