// Forma vieja de declarar arreglos o arrays
console.log('');
// 1.1 Arreglos en JavaScript
let autos = new Array('Renault', 'Peugeot', 'Ford', 'Dodge');
console.log(autos);

// Forma actual de declarar arreglos
const nuevosAutos = ['Ferrary', 'volkswagen', 'bmw', 'jeep'];
console.log(nuevosAutos);
console.log(nuevosAutos[1]);

console.log('');
console.log('1.2 Recorremos los elementos de un arreglo');
// Recorremos los elementos de un arreglo
for( i = 0; i < nuevosAutos.length; i++) {
    console.log(i + ' : ' + nuevosAutos[i]);
}

console.log('');
console.log('1.3 Modificamos los elementos');
nuevosAutos[1] = 'Renault';
for( i = 0; i < nuevosAutos.length; i++){
    console.log(i + ' : ' + nuevosAutos[i]);
}

console.log('');
console.log('Agregamos nuevo elemento al arreglo (AL FINAL)');
nuevosAutos.push('Audi');
console.log(nuevosAutos);

// Otra forma de agregar elementos al arreglo, utilizando el largo del arreglo
console.log('');
autos[autos.length] = 'Porsche';
console.log(autos);

console.log('');
// Otra forma: TENER CUIDADO porque se salta lugares agregando lugares vacios
autos[6] = 'Fiat';
console.log(autos);
autos[15] = 'Volvo';
console.log(autos);

console.log('');
// 1.4 Preguntar si es un Array
console.log(typeof(autos));     // vemos deque tipo es autos, nos dice que es de tipo object
console.log(Array.isArray(autos));  // Preguntamos, de la clase Array, es array autos?
console.log(autos instanceof Array);    //Preguntamos si autos es una instancia de la clase Array

console.log('Fin clase arreglos');