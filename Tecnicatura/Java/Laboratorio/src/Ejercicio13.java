import java.util.Scanner;

public class Ejercicio13 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] tablaOriginal = new int[10];
        int[] tablaSeparada = new int[10];
        int indicePares = 0;
        int indiceImpares = 0;

        // Leer los 10 elementos desde el teclado
        System.out.println("Ingrese 10 números enteros:");
        for (int i = 0; i < 10; i++) {
            System.out.print("Elemento " + (i + 1) + ": ");
            tablaOriginal[i] = scanner.nextInt();
        }

        // Llenar la tablaSeparada con los pares primero
        for (int i = 0; i < 10; i++) {
            if (tablaOriginal[i] % 2 == 0) {
                tablaSeparada[indicePares] = tablaOriginal[i];
                indicePares++;
            }
        }

        // Continuar llenando con los impares
        indiceImpares = indicePares; // Comenzar a partir del final de los pares
        for (int i = 0; i < 10; i++) {
            if (tablaOriginal[i] % 2 != 0) {
                tablaSeparada[indiceImpares] = tablaOriginal[i];
                indiceImpares++;
            }
        }

        // Mostrar la tabla separada
        System.out.println("Tabla separada (pares seguidos de impares):");
        for (int i = 0; i < 10; i++) {
            System.out.print(tablaSeparada[i] + " ");
        }
    }
}
