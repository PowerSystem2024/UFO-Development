/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
/*
Ejercicio 1: Leer un numero y mostrar su cuadrado, repetir el proyecto hasta que
se introduzca un nuimero negativo
*/
package Ciclos01;

import javax.swing.JOptionPane;


public class Ejercicio01 {
    public static void main(String[] args) {
         
        int numero, cuadrado;
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero >= 0 ){
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El numero "+numero+" elevado al cuadrado es: "+cuadrado);
           
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        System.out.println("El programa a finalizado por numero negativo");
    }
}
