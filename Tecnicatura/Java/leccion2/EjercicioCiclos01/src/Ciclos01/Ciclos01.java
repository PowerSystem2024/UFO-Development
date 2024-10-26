/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */ 
/*
Ejercicio 1: Leer un numero y mostrar su cuadrado, repetir el proyecto hasta que
se introduzca un nuimero negativo
*/
package Ciclos01;

import java.util.Scanner;

public class Ciclos01 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        int numero, cuadrado;
        System.out.println("Digite un numero");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero >= 0 ){
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El numero "+numero+" elevado al cuadrado es: "+cuadrado);
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El programa a finalizado por numero negativo");
    }
}
