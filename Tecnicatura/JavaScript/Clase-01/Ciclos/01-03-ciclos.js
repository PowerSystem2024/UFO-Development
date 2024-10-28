// Ciclo while
let contador = 0;
while(contador < 3){
    console.log(contador);
    contador++;                 // Operador unario de post incremento 
}                               //lo utilizamos para que cresta y no sea infinito 
console.log("Fin del ciclo while");

// Ciclo do while

let conteo = 0;
do{
    console.log(conteo);
    conteo++;      // Operador unario de post incremento 
    //lo utilizamos para que cresta y no sea infinito               
    
}while(conteo < 3);
console.log("Fin del ciclo do while");

// Ciclo for
for(let contando = 0; contando < 3 ; contando++ ){
    console.log(contando);
}
console.log("Fin del ciclo for");

// Palabra reservada break
for(let contando = 0; contando <= 10; contando++){
if(contando % 2 == 0){  // si el residuo entre dos es = 0 es par
        console.log(contando); 
        break;                 // Al encontrar el primer numero par rompe el ciclo for
    }
}
console.log("Termina el ciclo al encontrar el primer numero par")

// La palabra continue 

for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 !== 0){     //cuando es un numero impar
        continue;               // Ignora el numero par, va a la siguiente iteracion  
    }                           // E imprime por consola todos los pares
    console.log(contando);
}
console.log("Termina el ciclo")

//La palabra continue y Etiquetas Labels

inicio:
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 !== 0){     
        break inicio;           // Va a la siguiente iteracion               
    }                           
    console.log(contando);
}
console.log("Termina el ciclo")
//no son muy recomendadas para la programacion, es lo que se conoce como algoritmo go to 