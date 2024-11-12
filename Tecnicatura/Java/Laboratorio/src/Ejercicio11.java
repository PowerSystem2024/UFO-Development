import java.util.Scanner;

public class Ejercicio11 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] tabla = new int[10];
        int numElementos = 5;  // Actualmente solo tenemos 5 elementos en la tabla de tamaño 10

        // Leer 5 elementos ordenados de forma creciente
        System.out.println("Ingresa 5 números en orden creciente:");
        for (int i = 0; i < numElementos; i++) {
            tabla[i] = scanner.nextInt();
        }

        // Leer el nuevo número a insertar
        System.out.println("Ingresa el número a insertar:");
        int nuevoNumero = scanner.nextInt();

        // Encontrar la posición adecuada para insertar el nuevo número
        int posicion = 0;
        while (posicion < numElementos && tabla[posicion] < nuevoNumero) {
            posicion++;
        }

        // Desplazar los elementos hacia la derecha para hacer espacio
        for (int i = numElementos; i > posicion; i--) {
            tabla[i] = tabla[i - 1];
        }

        // Insertar el nuevo número en la posición adecuada
        tabla[posicion] = nuevoNumero;
        numElementos++;  // Incrementar el número de elementos en la tabla

        // Mostrar la tabla resultante
        System.out.println("Tabla después de insertar el nuevo número:");
        for (int i = 0; i < numElementos; i++) {
            System.out.print(tabla[i] + " ");
        }

        scanner.close();
    }
}