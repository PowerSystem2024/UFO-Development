/*
Ejercicio 5: Realizar un juevo para adivinar un numero;
para ello generar un numero aleatorioentre 0 y 100, y
luego ir pidienfo numeroa indicando  "es mayor" o
"es menor" segun sea mayor o menor con respecto a N
El proceso termina cuando el usuario acierta  y mostramos
el numero de intentos hechos
*/
package Ciclos05;

import java.util.Scanner;


public class Ciclos05 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, aleatorio, conteo = 0;
        aleatorio = (int)(Math.random()*100); //Esto genera un numero aleatoriuo
        do{
            System.out.println("Digite un numero: ");
            numero = Integer.parseInt(entrada.nextLine());
            if(numero < aleatorio){
                System.out.println("Digite un numero mayor");
            }
            else if(numero > aleatorio){
                System.out.println("Digite un numero menor");
            }
            else{
                System.out.println("Felicidades!!! Has adivinado el numero");
            }
            conteo++;
        } while (numero != aleatorio);
        
        System.out.println("Adivinate el numero en: "+conteo+" intentos");
    }
}
