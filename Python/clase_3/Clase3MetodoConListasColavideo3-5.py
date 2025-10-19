# Colas con listas
# Estructuras de datos de tipo  FIFO(first input/first output)
# Existe una forma establecida en python, importando el modo coleccion pero ahora no lo vamos a hacer así

cola=["Ariel", "Osvaldo","Liliana","Pilar"]

#Agregamos elementos al final de la cola
cola.append("Natalia")
cola.append("José")
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente {seRetira}')
print(cola)