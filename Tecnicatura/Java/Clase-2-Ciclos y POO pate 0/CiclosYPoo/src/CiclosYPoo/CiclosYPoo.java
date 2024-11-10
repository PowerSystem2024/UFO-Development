/*
 Ejercicio 1: Leer un número y mostrar su cuadrado, repetir
 el proceso hasta que se introduzca un número negativo   
 */
package CiclosYPoo;

import java.util.Scanner;

/**
 *
 * @author Dario.B
 */
public class CiclosYPoo {
    public static void main(String[] args) {
        
        Scanner entrada = new Scanner(System.in);                         // Se crea una instancia de la clase scanner llamada entrada que puede ser leída desde la consola de comandos(System.in)
        int numero, cuadrado;                                                   // se crean dos variables enteras, numero y cuadrado.
        System.out.println("Digite un número: ");
        numero = Integer.parseInt(entrada.nextLine());                        // se lee una entrada y se convierte el valor a entero
        while(numero >= 0) {
            cuadrado = (int)Math.pow(numero,2 );
            System.out.println("EL numero " + numero + " elevado al cuadrado es: " + cuadrado);
            System.out.println("Digite otro número: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El programa a finalizado por número negativo");
        
        // *******************************************************
        System.out.println("Practica para reforzar!");
        
        // primero creo la instancia donde guardo la entrada
        Scanner entrada2 = new Scanner(System.in);
        // Luego creo una variable para guardar mi dato de entrada
        String dato1;
        int dato2;
        // hago el ingreso del dato por consola de comandos de dos maneras:
        // Em ambos casos voy a ingresar un número pero en uno de ellos
        // lo voy a imprimir como string y en el otro como un valor cte.
        System.out.println("Ingrese el dato para ser impreso como string: ");
        dato1 = entrada2.nextLine();
        System.out.println("El dato como string es: " + dato1);
        
        System.out.println("Ingrese el dato para ser impreso como nro. entero: ");
        dato2 = Integer.parseInt(entrada2.nextLine());
        System.out.println("El dato como Nro entero es: " + dato2);
        // *******************************************************
        
        
    }
}
