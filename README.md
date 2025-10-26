# Grupo Rebelde Bug 💻🐞

Somos el grupo **Rebelde Bug**, un equipo de estudiantes de la UTN trabajando de forma colaborativa en las actividades de las clases.  
En este repositorio iremos subiendo los ejercicios, proyectos y prácticas desarrolladas en conjunto.

## Integrantes 👥
- Camila Scheurer  
- Zoé Geraldine Garnica  
- Maximiliano Foglia  
- Rubén Marchisio  
- José Cueva  
- Melina Denise Gallo  
- Aramayo Micaela Cynthia  
- Ivana Daniela Molina  
- Jimena Karin Pérez  

---
---

## 📑 Índice de clases

- [Clase 1 - Uso de GitHub](#clase-1---uso-de-github)
- [Clase 2 - Configuración de SSH y ramas en GitHub](#clase-2---configuración-de-ssh-y-ramas-en-github)
- [Clase 3 - Cambios en GitHub: de master a main](#clase-3---cambios-en-github-de-master-a-main)
- [Clase 04 - Tu primer push](#-clase-04)
- [Clase 05 - Git tag y versiones en GitHub](#-clase-05)

## Objetivo 🚀
Este repositorio será nuestro espacio de trabajo grupal donde subiremos las **actividades de las clases** para organizarnos mejor y mantener un registro del progreso de todos.  

---

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
# Clase 3 - Cambios en GitHub: de *master* a *main*

El escritor argentino **Julio Cortázar** afirma que las palabras tienen *color* y *peso*.  
Por otro lado, los sinónimos existen por definición, pero no expresan lo mismo:  
- **Feo** no es lo mismo que **desagradable**.  
- **Aromático** no es lo mismo que **oloroso**.  

👉 Los sinónimos no expresan lo mismo, no tienen el mismo “color” ni el mismo “peso”.  
Y sí, esta reflexión también forma parte de la enseñanza profesional de **Git & GitHub**.

---

## 1. Contexto del cambio

Desde el **1 de octubre de 2020**, GitHub cambió el nombre de la rama principal:  
- Antes: `master`  
- Ahora: `main`  

Este cambio surge como consecuencia del movimiento **#BlackLivesMatter**, ya que la industria tecnológica ha usado durante años términos como *master/slave*, *blacklist/whitelist*, los cuales hoy se busca reemplazar por expresiones más inclusivas.  

**Las palabras importan.**  
Por lo tanto, de aquí en adelante, cada vez que encuentres la palabra *master* debes entender que se refiere a *main*.  

---

## 2. ¿Cuándo sigue siendo `master` y cuándo es `main`?

### ➤ Al crear repositorios **localmente** (con `git init`)
- La rama por defecto sigue siendo **`master`**.  
- Para cambiarla a `main`, usamos:  
  ```bash
  git branch -M main
  ```

- Para que siempre usemos `main` por defecto en cualquier proyecto:  
  ```bash
  git config --global init.defaultBranch main
  ```

👉 A partir de ese momento, cada vez que uses `git init`, la rama inicial será `main`.  

---

### ➤ Al crear repositorios **desde GitHub (en la nube)**
- GitHub ya establece automáticamente la rama principal como **`main`**.  
- Al clonar un repositorio, se mantendrá con ese nombre.  
- Por lo tanto, **no será necesario realizar ningún cambio**.  

---

## 3. Visualización de ramas con `gitk`

El comando `gitk` permite visualizar de forma gráfica la historia de commits y ramas.  

Si no funciona al ejecutarlo, probablemente no esté instalado por defecto.  

### Instalación en Linux:
```bash
sudo apt-get update
sudo apt-get install gitk
```

---

## 📌 Resumen

- **GitHub usa `main` por defecto desde 2020.**  
- Si creamos repositorios localmente con `git init`, debemos configurar o renombrar `master` a `main`.  
- Podemos automatizar el uso de `main` con:  
  ```bash
  git config --global init.defaultBranch main
  ```  
- `gitk` es una herramienta útil para visualizar el historial de Git, aunque requiere instalación adicional en algunos sistemas.  

---

# 📚 Clase 04  

## 🔹 Tu primer push  

La creación de las **llaves SSH** es necesaria **solo una vez por cada computadora**.  
Aquí aprenderás cómo conectar a GitHub usando SSH de forma segura, sin necesidad de escribir usuario y contraseña todo el tiempo.  

---

## 🔑 Configuración de SSH en GitHub  

1. Crea tus llaves SSH en tu computadora.  
2. Copia la **llave pública**.  
3. Entra a **GitHub → Configuración → SSH and GPG Keys**.  
4. Crea una nueva llave:  
   - Asigna un **nombre descriptivo** (ej: *Mi Laptop*).  
   - Pega el contenido de la llave pública.  

Ahora podemos actualizar la URL que guardamos en nuestro repositorio remoto, pero usando **SSH en vez de HTTPS**:  

```bash
git remote set-url origin url-ssh-del-repositorio-en-github
```

---

## 📋 Comandos para copiar la llave SSH pública  

- **Mac**:  
  ```bash
  pbcopy < ~/.ssh/id_rsa.pub
  ```

- **Windows (Git Bash)**:  
  ```bash
  clip < ~/.ssh/id_rsa.pub
  ```

- **Linux (Ubuntu)**:  
  ```bash
  cat ~/.ssh/id_rsa.pub
  ```

---

## ⚠️ Importante  

Las buenas prácticas nos enseñan que **antes de hacer un `push` siempre debemos hacer un `pull` o un `fetch`**,  
para evitar conflictos en caso de que alguien ya haya hecho cambios en el repositorio.  

---

## 👥 Invitar a un colaborador  

Para invitar a un colaborador en GitHub:  

1. Ve al repositorio → **Settings**.  
2. Selecciona **Collaborators**.  
3. Ingresa tu contraseña o código de verificación **2FA**.  
4. Envía la invitación escribiendo el **nombre de usuario** del colaborador.  

👉 Del otro lado, el usuario solo debe **aceptar la invitación** y ya podrá participar en el proyecto haciendo commits.  

---

# 📚 Clase 05  

## 🏷️ Git tag y versiones en GitHub  

En Git, las **etiquetas (tags)** tienen un papel importante al asignar **versiones a los commits más significativos** de un proyecto.  

Aprender a utilizar `git tag`, entender los diferentes tipos de etiquetas, cómo **crearlas, listarlas, eliminarlas y compartirlas**, es esencial para un flujo de trabajo eficiente.  

---

## ✨ Creación de etiquetas en Git  

```bash
git tag nombre-etiqueta
```

📌 Sustituye `nombre-etiqueta` con un identificador semántico que refleje el estado del repositorio en ese momento (ej: `v1.0.0`).  

### Tipos de etiquetas:  
- **Anotadas**: almacenan información adicional como fecha, usuario y correo. Son ideales para **releases públicas**.  
- **Ligeras**: funcionan como marcadores simples de un commit.  

---

## 📋 Listar etiquetas existentes  

```bash
git tag
```

Ejemplo de salida:  

```
v1.0
v1.1
v1.2
```

También puedes filtrar etiquetas con expresiones comodín:  

```bash
git tag -l "v1.*"
```

---

## 🔄 Compartir etiquetas en remoto  

Por defecto, las etiquetas **no se envían automáticamente** a GitHub.  

- Enviar una etiqueta específica:  
  ```bash
  git push origin nombre-etiqueta
  ```

- Enviar **todas las etiquetas** a la vez:  
  ```bash
  git push origin --tags
  ```

---

## ❌ Eliminación de etiquetas  

- Eliminar en **local**:  
  ```bash
  git tag -d nombre-etiqueta
  ```

- Eliminar en **remoto**:  
  ```bash
  git push origin --delete nombre-etiqueta
  ```

---

## ✅ Resumen  

Las etiquetas en Git son esenciales para:  
- Asignar **versiones** al proyecto.  
- Capturar **momentos importantes** en el historial.  
- Facilitar un **flujo de trabajo ordenado** para releases y despliegues.  

👉 Aprender a **crear, listar, compartir y eliminar** etiquetas mejora tu control sobre las versiones de tu proyecto.

# 📚 Clase 06 y 07

# Error de duplicado de tags en Git

## ¿Un tag se puede generar dos veces?
👉 **No.**  
En el repositorio local, Git no te deja crear dos veces el mismo nombre de *tag*.  
Si intentás, te da error:

```
fatal: tag 'v1.0' already exists
```

---

## ¿Por qué aparece el error de “dos tags con el mismo nombre”?

El problema no está en la PC, sino cuando hay **dos definiciones diferentes del mismo tag en contextos distintos**:

### Local vs. remoto
- En tu PC tenés `v1.0` apuntando a un commit.  
- En el remoto (GitHub, GitLab) alguien creó también `v1.0` pero apuntando a otro commit.  
- Cuando hacés `git push --tags`, Git detecta el choque y dice: “hay dos tags distintos con el mismo nombre”.

### Entre distintas personas del equipo
- Cada uno pudo haber creado un tag con el mismo nombre pero sobre commits diferentes.  
- Al subirlos al mismo remoto, se genera la colisión.

### Tipos distintos de tag
- Uno pudo ser **ligero** y otro **anotado**, ambos con el mismo nombre.  
- Aunque se llamen igual, Git los trata como objetos diferentes.

---

## Ejemplo paso a paso en consola

### 👤 En PC 1
```bash
# Hacés un commit
git commit -m "Mi versión estable"

# Creás el tag v1.0
git tag v1.0

# Subís el tag al remoto
git push origin v1.0
```

👉 Ahora en GitHub existe `v1.0` apuntando a tu commit.

---

### 👤 En PC 2
```bash
# Hace otro commit distinto
git commit -m "Otra versión estable"

# También crea un tag con el mismo nombre
git tag v1.0

# Intenta subirlo
git push origin v1.0
```

👉 Git responde:
```
! [rejected]        v1.0 -> v1.0 (already exists)
error: failed to push some refs to 'github.com:repo.git'
```

---

## ⚠️ ¿Qué pasó?
- En local de PC 2: `v1.0` apunta a su commit.  
- En remoto: `v1.0` ya existe, apuntando al commit de PC 1.  
- Git detecta que son dos tags diferentes con el mismo nombre → **conflicto**.

---

## ✅ Solución
PC 2 debe borrar el tag local y recrearlo, o bien coordinar con el equipo qué commit debe llevar el nombre `v1.0`.

### Ejemplo para borrar y recrear:
```bash
git tag -d v1.0              # Borrar tag local
git fetch origin --tags      # Traer el correcto del remoto
```

### Si el tag remoto estaba mal y hay que corregirlo:
```bash
git tag -d v1.0
git tag v1.0 <commit_correcto>
git push origin :refs/tags/v1.0   # Borrar en remoto
git push origin v1.0              # Subir tag correcto
```

---