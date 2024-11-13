import java.util.Arrays;

public class Ejercicio14 {
    public static void main(String[] args) {
        int[] array1 = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}; // Primer arreglo ordenado
        int[] array2 = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}; // Segundo arreglo ordenado
        int[] mergedArray = new int[array1.length + array2.length];

        int i = 0, j = 0, k = 0;

        // Fusionar los arreglos
        while (i < array1.length && j < array2.length) {
            if (array1[i] < array2[j]) {
                mergedArray[k++] = array1[i++];
            } else {
                mergedArray[k++] = array2[j++];
            }
        }

        // Copiar los elementos restantes de array1 si los hay
        while (i < array1.length) {
            mergedArray[k++] = array1[i++];
        }

        // Copiar los elementos restantes de array2 si los hay
        while (j < array2.length) {
            mergedArray[k++] = array2[j++];
        }

        // Imprimir el arreglo fusionado
        System.out.println("Arreglo fusionado y ordenado: " + Arrays.toString(mergedArray));
    }
}
