import java.util.Scanner;

public class Ejercicio4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] numeros = new int[10];

        // Leer los 10 números y guardarlos en el arreglo
        System.out.println("Ingresa 10 números enteros:");
        for (int i = 0; i < 10; i++) {
            numeros[i] = scanner.nextInt();
        }

        // Mostrar los números en el orden requerido
        System.out.println("Números en el orden requerido:");
        for (int i = 0; i < 5; i++) {
            System.out.print(numeros[i] + " ");           // Muestra el i-ésimo elemento
            System.out.print(numeros[9 - i] + " ");       // Muestra el elemento en la posición 9 - i
        }

        scanner.close();
    }

}
