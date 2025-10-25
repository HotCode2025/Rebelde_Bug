Nombre del archivo principal:
JuegoDelAhorcado.java

Lenguaje:
Java

Descripción:
Este programa implementa el clásico Juego del Ahorcado, donde el jugador debe adivinar una palabra oculta letra por letra.
Cada error suma un intento fallido y si el jugador alcanza el límite de intentos permitidos, pierde la partida.
Si logra adivinar todas las letras antes de agotar los intentos, gana.

Contenidos del archivo

El código incluye:

Uso de clases y métodos (JuegoDelAhorcado).
Uso de arrays de caracteres para manejar las letras de la palabra.
Control de errores y validaciones.
Mensajes interactivos por consola.

Instrucciones para la ejecución del programa

El presente proyecto corresponde al desarrollo del juego “Juego del Ahorcado”, implementado en lenguaje Java.
A continuación, se detallan los pasos necesarios para compilar y ejecutar correctamente el programa en cualquier entorno que disponga del compilador de Java.

Requisitos previos

Antes de ejecutar el programa, es necesario contar con:

Java Development Kit (JDK) instalado en el sistema (versión 8 o superior).
Un entorno de desarrollo o editor de texto, como Visual Studio Code o cualquier otro compatible con Java.
El archivo fuente denominado JuegoDelAhorcado.java ubicado en una carpeta accesible (por ejemplo: C:\Users\Usuario\tecnicatura\Proyecto_Integrador).
Para verificar que Java se encuentra correctamente instalado, puede ejecutarse el siguiente comando en la terminal o consola del sistema:

java -version

Compilación del programa:

Abrir una terminal o consola de comandos.
Acceder al directorio donde se encuentra almacenado el archivo del proyecto. Por ejemplo:

cd C:\Users\Usuario\tecnicatura\Proyecto_Integrador

Compilar el archivo utilizando la codificación UTF-8 (recomendado para evitar errores con caracteres acentuados o especiales):

javac -encoding UTF-8 JuegoDelAhorcado.java

Si la compilación fue exitosa, se generará un archivo JuegoDelAhorcado.class en el mismo directorio.

Una vez compilado, el programa puede ejecutarse mediante el siguiente comando:

java JuegoDelAhorcado

El sistema iniciará el juego en la consola, mostrando el menú de temáticas disponibles y solicitando la interacción del usuario.

Resumen de Juego:
El Juego del Ahorcado es una aplicación de consola que permite al usuario poner a prueba sus conocimientos y habilidades para adivinar palabras ocultas, relacionadas con distintas temáticas disponibles (por ejemplo: Medicina, Cine/Series y Música).

Al iniciar el programa, el sistema muestra un menú de selección de temáticas, a partir del cual el jugador puede elegir la categoría de palabras con la que desea jugar.
El juego selecciona una palabra de forma aleatoria y muestra una serie de guiones bajos (_), representando las letras por descubrir.

El usuario deberá ingresar letras una por una hasta completar correctamente la palabra o agotar la cantidad de intentos permitidos.
Si la letra ingresada pertenece a la palabra, el sistema revelará su posición; en caso contrario, se descontará un intento disponible.

El objetivo del juego es adivinar la palabra completa antes de que el personaje sea “ahorcado”, simbolizando la pérdida de la partida.
Una vez finalizado el juego, el sistema ofrece la posibilidad de volver al menú principal o salir del programa.