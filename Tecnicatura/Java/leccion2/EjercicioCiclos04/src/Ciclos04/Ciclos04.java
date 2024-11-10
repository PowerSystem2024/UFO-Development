/*
Ejercicio 4: Pedir un numero hasta que s e teclee un numero negativo, 
y mostrar cuantos numeros se han introducido
Lo hacemos primero con la clase scanner y 
luego lo hacemos con la clase JOptionPane
*/
package Ciclos04;

import java.util.Scanner;


public class Ciclos04 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, conteo = 0;
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero >= 0 ){
            System.out.println("El numero es positivo");
            conteo++;
            System.out.println("Digite otro numero");
            numero = Integer.parseInt(entrada.nextLine());
                
        }
        System.out.println("A ingresa "+conteo+" numeros que no negativos");
    }
}
