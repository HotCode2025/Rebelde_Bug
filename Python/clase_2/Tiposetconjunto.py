#Tipo set
planetas = {"Marte", "Jupiter", "Venus"}
print(len(planetas)) #Usamos la funcion len=lenght significa largo


print("Marte" in planetas) #Tambien podemos preguntar si no está con "not in"

#Agregar un elemento
planetas.add("Tierra") #Add es una funcion
planetas.add("Tierra")
print(planetas)

#Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove("Jupiter") #Esta funcion ante un mal ingreso u inexistencia del elemento da error
print(planetas)
planetas.discard("tierra")#Esta funcion no nos presenta ningun error
print(planetas)

#Limpiar set
planetas.clear()
print(planetas)

#Eliminar set
del planetas
print(planetas)

