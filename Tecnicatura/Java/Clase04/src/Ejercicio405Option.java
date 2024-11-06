//Ejercicio 6: Pedir números hasta que se teclee un 0, mostrar
//la suma de todos los numeros introducidos.

import javax.swing.JOptionPane;

public class Ejercicio405Option {
    public static void main(String[] args) {
         
        int suma = 0; //Inicializamos la variable suma en 0
        int numero; //Declaramos la variable numero

        //Bucle para pedir números al usuario
        do {
            suma += numero;

        }while(numero !=0);
        JOptionPane.showMessageDialog(null,"La suma de los numeros ingresados es:"+suma);
        
    }

}