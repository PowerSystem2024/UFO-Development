/*
Ejercicio 5: Realizar un juevo para adivinar un numero;
para ello generar un numero aleatorioentre 0 y 100, y
luego ir pidienfo numeroa indicando  "es mayor" o
"es menor" segun sea mayor o menor con respecto a N
El proceso termina cuando el usuario acierta  y mostramos
el numero de intentos hechos
*/
package Ciclos05;

import javax.swing.JOptionPane;


public class Ejercicio05 {
    public static void main(String[] args) {
        int numero, aleatorio, conteo = 0;
        aleatorio = (int)(Math.random()*100); //Esto genera un numero aleatoriuo
        do{
           
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
            if(numero < aleatorio){
               JOptionPane.showMessageDialog(null, "Digite un numero mayor");
            }
            else if(numero > aleatorio){
                JOptionPane.showMessageDialog(null, "Digite un numero menor");
            }
            else{
                JOptionPane.showMessageDialog(null, "¡¡¡Felicidades!!! Has adivinado el numero");
            }
            conteo++;
        } while (numero != aleatorio);
        
        JOptionPane.showMessageDialog(null, "Adivinate el numero en: "+conteo+" intentos");
    }
}
