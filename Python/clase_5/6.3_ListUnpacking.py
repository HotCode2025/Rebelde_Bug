def show(name, lastName):
    print(name+' '+lastName)
person = ['Melina', 'Gallo']

show(person[0], person[1]) #Pasamos uno por uno los datos de la lista a la función
show(*person) #Esto es lo mismo que lo anterior pero pasamos TODO JUNTO
person2 = ['Rubén', 'Marchisio'] #Desempaquetamos a través de tupla
show(*person2)
person3 = {'lastName': 'Foglia', 'name': 'Maximiliano'}
show(**person3)