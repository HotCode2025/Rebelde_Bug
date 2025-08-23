# Clase 1 - Uso de GitHub

GitHub es una plataforma que nos permite guardar repositorios de Git que podemos usar como **servidores remotos** y ejecutar algunos comandos de forma visual e interactiva (sin necesidad de la consola de comandos).

Con GitHub podemos:

- Crear o importar repositorios.
- Crear organizaciones y proyectos de trabajo.
- Descubrir repositorios de otras personas.
- Contribuir a proyectos.
- Dar estrellas a repositorios.
- Muchas otras funcionalidades.

---

## Comandos y conceptos básicos

- **Import repository**: importar un repositorio existente.  
- **New repository**: crear un nuevo repositorio.  
- **New organization**: equivalente a una empresa o grupo de trabajo.  
- **New project**: un grupo de repositorios dentro de una organización.  
- **New gist**: fragmento de código que se comparte fácilmente.  

### Crear un nuevo repositorio
1. Click en **New repository**.  
2. Nombre: `Prueba-Inicio.Repo`.  
3. Descripción: "Así armamos un repositorio".  
4. Elegir si será **privado** o **público**.  
5. Opcional: agregar un archivo `README.md` y un `.gitignore`.  

---

## El archivo README.md

El **README.md** es el archivo que veremos por defecto al entrar a un repositorio.  
Es una muy buena práctica configurarlo para describir el proyecto, los requerimientos y las instrucciones para contribuir correctamente.

---

## Clonar un repositorio

Para clonar un repositorio desde GitHub:

```bash
git clone <URL-SSH>
```

Esto descargará la versión del proyecto que se encuentra en GitHub.

⚠️ **Atención**:  
- Con **HTTPS** pedirá usuario y contraseña (ya no funciona fácilmente).  
- Lo recomendable es usar **SSH**.  

---

## Conectar un repositorio remoto a local

👉 Importante: **no usar `git init` si ya trabajaremos con un repositorio creado en GitHub**.  
En su lugar, debemos ejecutar estos pasos:

1. Crear el repositorio en GitHub.  
2. Copiar el enlace **SSH**.  
3. Abrir **Git Bash** como administrador.  
4. Navegar hasta el directorio de trabajo:

```bash
ll
cd Documents
mkdir Proyectos
cd Proyectos
```

5. Clonar el repositorio:

```bash
git clone <URL-SSH>
```

6. Entrar al repositorio:

```bash
cd Prueba-Inicio-Repo
```

---

## Actualizar desde la nube

```bash
git pull origin main
```

o bien:

```bash
git fetch
```

---

## Crear y gestionar archivos

Crear un archivo `README.md`:

```bash
touch README.md
```

Verificar si existe:

```bash
ll
ls
```

---

## Flujo básico de trabajo con Git

1. Ver el estado actual:
   ```bash
   git status
   ```

2. Agregar cambios:
   ```bash
   git add .
   ```

3. Confirmar cambios:
   ```bash
   git commit -m "Mensaje del commit"
   ```

4. Subir cambios a la nube:
   ```bash
   git push origin main
   ```

5. Refrescar la página de GitHub (**F5**) para ver los cambios reflejados.

---

## Consejos de seguridad y configuración

- Autenticación en dos pasos para proteger la cuenta.  
- Generar **clave pública y privada** para cada ordenador.  
- Mantener copias de seguridad de las claves.  
- Colocar siempre un `README.md` y un `.gitignore` en los repositorios.  

---

## GitHub como red social

- Podemos dar ⭐ a proyectos que nos gustan.  
- Descubrir nuevos repositorios.  
- Con un simple **`.` (punto)** en cualquier repositorio, se abre **Visual Studio Code en el navegador**. 🚀  

---
# Clase 2 - Configuración de SSH y ramas en GitHub

En esta clase aprenderemos a **cargar una llave SSH pública en GitHub** y a configurar ramas en nuestro repositorio.

---

## 1. Copiar la llave SSH pública

1. Ir al directorio `.ssh` en tu computadora.  
   - Allí encontrarás un archivo con extensión `.pub`.  
2. Abrir el archivo con un editor de texto (ejemplo: Bloc de notas).  
3. Copiar todo el contenido de la clave pública.

---

## 2. Agregar la llave en GitHub

1. Entrar a **GitHub → Settings → SSH and GPG keys**.  
2. Crear una nueva llave con **New SSH key**.  
3. Ponerle un **nombre descriptivo** (ejemplo: el nombre del ordenador).  
4. Pegar el contenido de la clave pública.  

⚠️ Recomendación:  
Cada PC o dispositivo nuevo que usemos debe tener su propia clave SSH cargada en GitHub.

---

## 3. Comandos útiles para ramas

Ver en qué rama estamos:
```bash
git branch
```

Cambiar a la rama `master`:
```bash
git checkout master
```

Renombrar la rama `master` a `main`:
```bash
git branch -M main
```

---

## 4. Conectar repositorio local a remoto

Agregar un repositorio remoto (ejemplo):
```bash
git remote add origin git@github.com:nombreUsuario/class-git.git
```

Verificar que el remoto esté conectado:
```bash
git remote -v
```

---

## 5. Fusionar ramas (merge)

Unir la rama `segunda` a `main`:
```bash
git merge segunda
```

---

## 6. Guardar y subir cambios

Hacer commit con mensaje:
```bash
git commit -am "Uso de GitHub parte 20"
```

Subir los cambios al remoto:
```bash
git push origin main
```

---

## 7. Cambio de rama principal en GitHub

Cuando cambiamos de `master` a `main`, puede pasar que en el repositorio remoto se creen dos ramas: **master** y **main**.  

Para solucionarlo:  
1. Ir al repositorio en GitHub.  
2. Abrir **Settings → Branches**.  
3. Cambiar la rama principal a `main`.  
4. Borrar la rama `master` (ya no será necesaria).  

---
