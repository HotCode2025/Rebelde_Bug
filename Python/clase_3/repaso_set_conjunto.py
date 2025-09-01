# -----------------------------------------------------------
# CONJUNTOS (set) clase 3 videos 3.1 (1,2,3)
# -----------------------------------------------------------
# Un conjunto es una colección de elementos que cumple con:
# NO tiene orden específico (no hay índices como en listas).
# NO permite duplicados (cada elemento aparece una sola vez).
# SE puede modificar (agregar o quitar elementos).
# -----------------------------------------------------------

# Definir conjuntos:
conjunto = set()            # Forma vacía: crea un conjunto sin elementos
conjunto1 = {'Hola'}        # Forma directa: conjunto con un elemento inicial

# -----------------------------------------------------------
# AGREGAR ELEMENTOS
# Usamos el método .add() para ingresar elementos.
# Si el elemento ya existe, no se agrega (se evita duplicados).

conjunto.add(7)
conjunto.add('Hola')
conjunto1.add(10)

print("Conjunto:", conjunto)     # {'Hola', 7}
print("Conjunto1:", conjunto1)   # {'Hola', 10}

# -----------------------------------------------------------
# PERTENENCIA DE ELEMENTOS
# Para verificar si un elemento está o no en un conjunto:

print(10 not in conjunto1)
print('Hola' in conjunto1)

# -----------------------------------------------------------
# IGUALDAD ENTRE CONJUNTOS
# Dos conjuntos son iguales si tienen los mismos elementos,
# sin importar el orden.

print(conjunto1 == conjunto)  

# -----------------------------------------------------------
# OPERACIONES ENTRE CONJUNTOS
# Unión (|) -> Combina todos los elementos de ambos conjuntos,
# sin duplicar elementos repetidos.

conjunto3 = conjunto | conjunto1
print("Unión:", conjunto3)

# Intersección (&) -> Devuelve los elementos que están en los dos conjuntos.
conjunto3 = conjunto & conjunto1
print("Intersección:", conjunto3)

# Diferencia (-) -> Devuelve los elementos que están en el primero,
# pero NO en el segundo.
conjunto3 = conjunto1 - conjunto
print("Diferencia:", conjunto3)

# Diferencia simétrica (^) -> Devuelve los elementos que están
# en uno u otro, pero NO en ambos.
conjunto3 = conjunto ^ conjunto1
print("Diferencia simétrica:", conjunto3)

# -----------------------------------------------------------
# SUBCONJUNTOS Y SUPERCONJUNTOS
# issubset() -> True si TODOS los elementos de un conjunto
# están contenidos dentro de otro.

conjunto3 = conjunto1 | conjunto  
print("¿conjunto1 es subconjunto de conjunto3?", conjunto1.issubset(conjunto3))
print("¿conjunto3 es subconjunto de conjunto?", conjunto3.issubset(conjunto))

# issuperset() -> True si un conjunto contiene a TODOS los
# elementos de otro (es el "superset").
print("¿conjunto3 es superconjunto de conjunto1?", conjunto3.issuperset(conjunto1))
print("¿conjunto3 es superconjunto de conjunto?", conjunto3.issuperset(conjunto))
print("¿conjunto1 es superconjunto de conjunto3?", conjunto1.issuperset(conjunto3))

# -----------------------------------------------------------
# CONJUNTOS DISJUNTOS
# isdisjoint() -> True si dos conjuntos NO tienen NINGÚN elemento en común.
print("¿conjunto y conjunto1 son disjuntos?", conjunto.isdisjoint(conjunto1))

# -----------------------------------------------------------
# CONJUNTOS INMUTABLES
# frozenset -> Crea un conjunto que NO se puede modificar.
# (No se pueden agregar ni eliminar elementos).
conjunto3 = frozenset({1, 2, 3})
print("Frozenset:", conjunto3)

