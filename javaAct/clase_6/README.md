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

## Equipo Rebelde Bug
- Camila Scheurer  
- Zoé Geraldine Garnica  
- Maximiliano Foglia  
- Ruben Marchisio  
- José Cueva  
- Melina Denise Gallo  
- Aramayo Micaela Cynthia  
- Ivana Daniela Molina  
- Jimena Karin Pérez
