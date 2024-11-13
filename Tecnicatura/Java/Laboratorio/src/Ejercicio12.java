import java.util.Scanner;

public class Ejercicio12 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] tabla = new int[10];

        // Leer los 10 elementos desde el teclado
        System.out.println("Ingrese 10 números enteros:");
        for (int i = 0; i < 10; i++) {
            System.out.print("Elemento " + (i + 1) + ": ");
            tabla[i] = scanner.nextInt();
        }

        // Leer la posición a eliminar
        int posicion;
        do {
            System.out.print("Ingrese la posición a eliminar (0-9): ");
            posicion = scanner.nextInt();
        } while (posicion < 0 || posicion >= 10);

        // Eliminar el elemento moviendo los siguientes elementos hacia la izquierda
        for (int i = posicion; i < tabla.length - 1; i++) {
            tabla[i] = tabla[i + 1];
        }

        // Mostrar la tabla actualizada sin el último elemento
        System.out.println("Tabla actualizada:");
        for (int i = 0; i < tabla.length - 1; i++) {
            System.out.print(tabla[i] + " ");
        }
    }
}