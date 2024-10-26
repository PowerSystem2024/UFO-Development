// Introducción a Funciones

mifuncion(8, 2); //Esto se lo conoce como hosting

function mifuncion(a, b){
    //console.log("Sumamos: "+ (a + b));
    return a + b;
}

//Llamando la funcion
mifuncion(5, 4);

let resultado = mifuncion(6, 7);
console.log(resultado);

// Declaramos una funcion de tipo expresion o anonima
let x = function(a, b){ return a + b}; // Necesita cierre con punto y coma
resultado = x(5, 6); // Al llamarla se pone la variable y parentesis
console.log(resultado);


// Funciones de tipo self y invoking
(function(a, b){
    console.log("Ejecutando la funcion: "+ (a + b));
})(9, 6);


console.log(typeof mifuncion);
function mifuncionDos(a, b){
    console.log(arguments.length);
}

mifuncionDos(5, 7, 3, 6);

//toString
var mifuncionTexto = mifuncion.toString();
console.log(mifuncionTexto);

// Funciones flecha
const sumarFuncionFlecha = (a, b) => a + b;
resultado = sumarFuncionFlecha(3, 7); //Asignamos el valor a una variable
console.log(resultado);


let sumar = function(a = 4, b = 8){
    console.log(arguments[0]); //muestra el parámetro a: 
    console.log(arguments[1]); //muestra el parámetro b: 
    return a + b + arguments[2];
}
resultado = sumar(3, 2, 9);
console.log(resultado); 

//Sumar todos los argumentos
let respuesta = sumarTodo(5, 4, 13, 10, 9);
console.log(respuesta); 

function sumarTodo() {
    let suma = 0;
    for (let i = 0; i < arguments.length; i++) {
        suma += arguments[i]; // arguments es para arreglos
    }
    return suma;
}

// Tipos primitivos
let k = 10;
function cambiarValor(a){ //Paso por valor
    a = 20;
}

cambiarValor(k);
console.log(k);

//Paso por referencia
const persona = {
    nombre: 'Pablo',
    apellido: 'Lopez'
};

console.log(persona);

function cambiarValorObjeto(p1) {
    p1.nombre = 'Nacho';
    p1.apellido = 'Pavez';
}

cambiarValorObjeto(persona);
console.log(persona);



