// Ciclo while
// En el ciclo while primero se revisa la condición y luego se ejecuta lo que está dentro del ciclo{}

console.log('EJECUCIÓN DEL CÓDIGO') // AGREGAMOS UN PRINT POR CONSOLA PARA INDICAR CADA VEZ QUE EJECUTO EL CÓDIGO

let contador = 0;               // inicializamos una variable contador en cero
while(contador < 3){
    console.log(contador);      // aqui esta la porción de codigo que se ejecuta dentro del ciclo while
    contador++;
}
console.log('Fin del ciclo while');

//do while
// En el ciclo do while primero se ejecuta lo que está dentro del ciclo{} y luego se revisa la condición
let conteo = 0;
do{
    console.log(conteo);
    conteo++;                   // operador unario de post increment
}while(conteo < 3);             // condición
console.log('Fin del ciclo do while');

// for
// A diferencia de los anteriores, en el ciclo for ya va a tener definidos el incremento o decremento del contador
// al igual que la variable que se incrementa o decrementa.

for( let contando = 0; contando < 3 ; contando++ ){         // esta parte se ve muy parecida o igual a java/python
    console.log(contando);
}
console.log('Fin del ciclo for');

// break
for( let contando = 0; contando < 10; contando++ ){
    if(contando % 2 == 0){
        console.log(contando);  // Buscamos mostrar los numeros pares por eso calculamos el residuo de dividir por 2 mediante un cond. if
    }
}
console.log('El ciclo finalilza al encontrar todos los números pares!');

// Si ponemos un break
for( let contando = 0; contando < 10; contando++ ){
    if(contando % 2 == 0){
        console.log(contando);  // Buscamos mostrar los numeros pares por eso calculamos el residuo de dividir por 2 mediante un cond. if
        break;
    }
}
console.log('Se muestra solo la primera ejecución del código y luego el break rompe cualquiera sea la estructura');   // Finalizando así el ciclo for

// La palabra continue y Etiquetas Labels
inicio:
for( let contando = 0; contando <= 10; contando++ ){
    if(contando % 2 !== 0){
        continue inicio;        //con la instrucción continue le decimos que si no es par que vuelva a la etiqueta inicio
    }
    console.log(contando);      // y si es par se imprimen solo los números pares, incluido el cero.-
}
console.log('Termina el ciclo');

// TAMBIEN PUEDO USAR brake en conjunto con break PARA HACER ROMPER EL CICLO FOR

inicio:
for( let contando = 0; contando <= 10; contando++ ){
    if(contando % 2 !== 0){
        break inicio;        //con la instrucción continue le decimos que si no es par que vuelva a la etiqueta inicio
    }
    console.log(contando);      // y si es par se imprimen solo los números pares, incluido el cero.-
}
console.log('Termina el ciclo');

// TAREA: TRAEMOS TODOS LOS EJERCICIOS DE CICLOS DE OTROS LENGUAJES PARA ESCRIBIRLOS AQUI CON LA SINTAXIS DE JAVASCRIPT.