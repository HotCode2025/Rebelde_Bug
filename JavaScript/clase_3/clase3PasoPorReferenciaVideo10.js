// 1.9.1 Paso por referencia (video 10)

const animal = {
    nombre: "Tigre",
    tipo: "Felino"
}
console.log(animal)

function cambioObjeto(a1){
    a1.nombre = "Jirafa",
    a1.tipo = "Jiráfido"
}

cambioObjeto(animal);
console.log(animal);