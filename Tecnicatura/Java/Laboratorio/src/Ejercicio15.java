import java.util.Arrays;
import java.util.Scanner;

public class Ejercicio15 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] array = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}; // Arreglo de 10 enteros ordenados

        System.out.print("Ingresa el número que deseas buscar: ");
        int N = scanner.nextInt();

        // Búsqueda del número N en el arreglo
        int posicion = Arrays.binarySearch(array, N);

        // Verificar si el número fue encontrado
        if (posicion >= 0) {
            System.out.println("Número encontrado en la posición: " + posicion);
        } else {
            System.out.println("El número no se encuentra en el arreglo.");
        }

        scanner.close();
    }
}
