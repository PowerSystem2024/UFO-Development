let x = 10; // Variable de tipo primitiva
console.log(x.length);
console.log("Tipos primitivos");
// Objeto
let persona = {
    nombre: 'Carla',
    apellido: 'Cuellos',
    email: 'ccuellos@gmail.com',
    edad: 20,
    idioma: "es",
    get lang(){
        return this.idioma.toUpperCase(); // Convierte las minusculas a mayuculas
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    },
    nombreCompleto: function(){ // Metodo o funcion en JavaScript
        return this.nombre+" "+this.apellido;
    },
    get nombreEdad(){ // Este es el metodo get
        return "El nombre es: "+this.nombre+" edad: "+this.edad;
    }
}

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);
console.log(persona.nombreCompleto());
console.log("Ejecutando con un objeto");
let persona2 = new Object(); // Debe crear un nuevo objeto en memoria
persona2.nombre = "Juaco";
persona2.direccion = "Salas 250";
persona2.telefono = "123456789";
console.log(persona2.telefono);
console.log("Creamos un nuevo objeto");
console.log(persona["apellido"]); // Accedemos como si fuera un arreglo
console.log("Usamos el ciclo for in");
// For in y accedemos al objeto como si fuera un arreglo
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);
}
console.log("Cambiamos y eliminamos un error");
persona.apellido = "Herrera"; // Cambiamos dinamicamente un valor del objeto
delete persona.apellido; // Eliminamos el error
console.log(persona);

// Distintas formas de imprimir un objeto
// Número 1: La más sencilla, concatenar cada valor de cada propiedad
console.log('Distintas formas de imprimir un objeto: forma 1');
console.log(persona.nombre + ', ' + persona.apellido);

// Número 2: A través del ciclo for in
console.log('Distintas formas de imprimir un objeto: forma 2');
for (nombrePropiedad in persona) {
    console.log(persona[nombrePropiedad]);
}

// Número 3: La función Object.values()
console.log('Distintas formas de imprimir un objeto: forma 3');
let personaArray = Object.values(persona);
console.log(personaArray);

// Número 4: Utilizando el método JSON.stringify
console.log("Distintas formas de imprimir un objeto: forma 4");
let personaString = JSON.stringify(persona);
console.log(personaString);

console.log("Comenzamos a utilizar el metodo get");
console.log(persona.nombreEdad);

console.log("Comenzamos con el metodo get para idiomas");
persona.lang = "en";
console.log(persona.lang);

function persona3(nombre, apellido, email){ // Contructor
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre+" "+this.apellido;
    }
}
let padre = new persona3("Lucas", "Castro", "castro@gmail.com");
padre.nombre = "Lemi"; // Modificamos el nombre
padre.telefono = "987654321"; // Una propiedad exclusiva del objeto padre
console.log(padre);
console.log(padre.nombreCompleto()); // Utilizamos la funcion
let madre = new persona3("Sofi", "Coti", "coti@gmail.com");
console.log(madre);
console.log(madre.telefono); // La propiedad no esta definida
console.log(madre.nombreCompleto());

// Diferentes formas de crear objetos

// Caso objeto 1
let miObjeto = new Object();  // Esta es una opción formal
// Caso objeto 2
let miObjeto2 = {};  // Esta opción es breve y recomendada

// Caso String 1
let miCadena1 = new String('Hola');  // Sintaxis formal
// Caso String 2
let miCadena2 = 'Hola';  // Esta es la sintaxis simplificada y recomendada

// Caso con números 1
let miNumero = new Number(1);  // Es formal pero no recomendable
// Caso con números 2
let miNumero2 = 1;  // Sintaxis recomendada

// Caso boolean 1
let miBoolean1 = new Boolean(false);  // Formal
// Caso boolean 2
let miBoolean2 = false;  // Sintaxis recomendada

//caso Arreglo 1
let miArreglo1 = new Array(); // Formal
//caso Arreglo 2
let miArreglo2 = []; // Sintaxis recomendada

// caso fuction 1
let miFuncion1 = new function(){}; //Todo despues de new es considerado objeto
// caso fuction 2
let miFuncion2 = function(){}; // Notacion simplificada y recomendada

// Uso de prototype
persona3.prototype.telefono = "101112131415";
console.log(padre);
console.log(madre.telefono);
madre.telefono = "1918171615";
console.log(madre.telefono);

// Uso de call
let persona4 = {
    nombre: "Juampi",
    apellido: "Pave",
    nombreCompleto2: function(titulo, telefono){
        return titulo+": "+this.nombre+" "+this.apellido+" "+telefono;
        //return this.nombre+" "+this.apellido;
    }   
}

let persona5 = {
    nombre: "Cesar",
    apellido: "Line"
}

console.log(persona4.nombreCompleto2("Line.", "212223242526"));
console.log(persona4.nombreCompleto2.call(persona5, "Ing.", "33323435"));

// Metodo Apply
let arreglo = ["Ing.", "40414445"];
console.log(persona4.nombreCompleto2.apply(persona5, arreglo));
