/*
Ejercicio 4: Pedir un numero hasta que s e teclee un numero negativo, 
y mostrar cuantos numeros se han introducido
Lo hacemos primero con la clase scanner y 
luego lo hacemos con la clase JOptionPane
*/
package Ciclos04;

import javax.swing.JOptionPane;


public class Ejercicio04 {
    public static void main(String[] args) {
        int numero, conteo = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero >= 0 ){
            JOptionPane.showConfirmDialog(null, "El numero es positivo");
            conteo++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
                
        }
        JOptionPane.showConfirmDialog(null, "A ingresado "+conteo+" numeros que no negativos");
       
    }
}
