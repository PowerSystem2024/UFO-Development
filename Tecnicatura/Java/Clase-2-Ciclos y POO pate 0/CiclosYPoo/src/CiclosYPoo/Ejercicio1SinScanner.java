/*
 Ejercicio 1: Leer un número y mostrar su cuadrado, repetir
 el proceso hasta que se introduzca un número negativo   
 */
package CiclosYPoo;

import javax.swing.JOptionPane;

/**
 *
 * @author Dario B.
 */
public class Ejercicio1SinScanner {
    public static void main(String[] args) {                        
        int numero, cuadrado;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número"));                
        while(numero >= 0) {
            cuadrado = (int)Math.pow(numero,2 );
            System.out.println("EL numero " + numero + " elevado al cuadrado es: " + cuadrado);
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número"));   // En esta linea damos al cambiar el nro, el while lo puede volver a analizar. Si no estuviese esta linea, el ciclo sería infinito.-
            
        }
        System.out.println("El programa a finalizado por número negativo");
        
    }
}
