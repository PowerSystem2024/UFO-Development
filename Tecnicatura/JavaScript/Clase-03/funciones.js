// Introducción a Funciones

//Llmamos a la funcion antes de crearla, "esto se conoce como hoisting"
miFuncion(10, 6); // Este resultado se mostrara primero

//Creamos la funcion
function miFuncion(a, b) {
  //console.log("Sumamos: " + (a + b)); // comentamos para que tome valor la palabra return
  return a + b;
}

//LLamamos la funcion
miFuncion(5, 4); //Le pasamos los valores que queremos que se sumen

let resultado = miFuncion(7, 8);
console.log(resultado);

//Declaramos una funcion de tipo expresión o funcion anonima
let x = function (a, b) {  return a + b}; // necesita estar cerrado con punto y coma
resultado = x(5, 6); // al llamar se pone la variable y parentesis
console.log(resultado);

//Funciones de tipo self o invoking
//se esta llamando asimisma
(function (a, b) {
  console.log("Ejecutando la funcion: " + (a + b));
})(9, 6); //No la podemos reutilizar

//Saber de que tipo es nuestra funcion y cuantos argumentos tiene
console.log(typeof miFuncionDos);
function miFuncionDos(a, b) {
  console.log(arguments);
}

miFuncionDos(5, 7);

//toString
var miFuncionString = miFuncionDos.toString();
console.log(miFuncionString);

//Funciones de tipo flecha
// No se utiliza la palabra reservada "function"
// No se utlizan las llaves
// No se utiliza la palabra "return"
const sumarFuncionFlecha = (a, b) => a + b;
resultado = sumarFuncionFlecha(3, 7); //Asignamos el valor a una variable
console.log(resultado);

//Funcion de tipo expresion
let sumar = function (a = 4, b = 8) {
  console.log(arguments[0]); //Muestra el parametro de a
  console.log(arguments[1]); //Muestra el parametro de b
  console.log(arguments[2]); 
  return a + b + arguments[2];
};
resultado = sumar(3, 2, 9);
console.log(resultado);

//Sumar todos los argumentos
let respuesta = sumarTodo(5, 4, 13, 10, 9);
console.log(respuesta);
function sumarTodo() {
  let suma = 0;
  for (let i = 0; i < arguments.length; i++){
    suma += arguments[i]; //arguments es para arreglos
  }
  return suma;
}


//Tipos primitivos
let k = 10;
function cambiarValor(a) {
  console.log(a)
  //Paso por valor
  a = 20;
  console.log(a)
}

cambiarValor(k);
console.log(k);

//Paso por referencia
const persona = {
  nombre: "Roberto",
  apellido: "Gonzalez",
};
console.log(persona);

function cambiarValorObjeto(p1) {
  p1.nombre = "Jose";
  p1.apellido = "Lepez";
}

cambiarValorObjeto(persona);
console.log(persona);
