//Creación de  Array o arreglos
//let autos = new Array("Ferrari", "Renault", "BMW") ;esta es la sintaxis vieja

const autos = ['Ferrari', 'Renault', 'BMW']; //Sintaxis actual
console.log(autos);

//Recorremos los elementos de un array (en forma manual)
console.log(autos[0]);
console.log(autos[2])

//si queremos recorrer tenemos que añadir un ciclo
for (let i = 0; i < autos.length; i++) {
  console.log(i + " : " + autos[i]);
}// + " : " +  es para concatenar 

//Modificar los elementos del array
autos[1] = 'Volvo';
console.log(autos[1]);

//Agregar nuevos valores al array
autos.push('Audi'); //Con el metodo ".push()" agregamos un elemento al final
console.log(autos);

//Otras formas de agregar elementos al array
autos[autos.length] = 'Porsche';
console.log(autos);

//Otra forma mas de agregar elementos teniendo cuidado.
autos[6] = 'Renault';
console.log(autos);

//Como preguntar si es un array
console.log(Array.isArray(autos)); //Devuelve un booleano

//Preguntamos si la variable es una instancia de la clase array
console.log(autos instanceof Array);
