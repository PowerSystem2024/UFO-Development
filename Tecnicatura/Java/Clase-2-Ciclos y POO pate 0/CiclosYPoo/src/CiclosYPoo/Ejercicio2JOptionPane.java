/*
Ejercicio 2: Leer un número e indicar si es positivo o negativo.
El proceso se repetira hasta que se introduzca un cero 0
 */
package CiclosYPoo;

import javax.swing.JOptionPane;

/**
 *
 * @author Dario B.
 */
public class Ejercicio2JOptionPane {
    public static void main(String[] args) {
        int num;
        do {
            num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
            
            if (num < 0) {
                System.out.println("El número ingresado es NEGATIVO!");
            } else if (num > 0) {
                System.out.println("El número ingresado es POSITIVO!");
            }
        } while (num != 0);   
      }   
    }
// ESTA CLASE FALTA TERMINAR. FALTA CONTINUAR CON EL DESARROLLO DEL EJERCICIO.
