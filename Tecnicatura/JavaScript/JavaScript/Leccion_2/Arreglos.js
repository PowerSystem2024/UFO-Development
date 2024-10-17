
// Arreglos en JavaScript
//let autos = new Array("Ford", "Toyota", "Hilux"); esta es la sintaxis viejas
const autos = ["Ford", "Toyota", "Hilux"];
console.log(autos);

//Recorremos los elementos de un arreglo
console.log(autos[0]);
console.log(autos[2]);

for(let i = 0; i < autos.length; i++){
    console.log(i+" : "+autos[i]);
}

// Modificamos los elementos
autos[1] = "Volvo";
console.log(autos[1]);

//Agregamos nuevos valores al arreglo
autos.push("Lamborghini"); // Agregamos el elemento al final del arreglo
console.log(autos);

// Otras formas de agregar elementos al arreglo
autos[autos.length] = "Porche";
console.log(autos);

// Tercera forma de agregar elementos teniendo CUIDADO
autos[6] = "Renault";
console.log(autos);

// Como preguntar si es una Array o Arreglo
console.log(Array.isArray(autos)); //Devuelve un booleano


console.log(autos instanceof Array); // Preguntamos si la variable es una instacia de la clase Array
