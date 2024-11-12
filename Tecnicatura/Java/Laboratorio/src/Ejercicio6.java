import java.util.Random;

public class Ejercicio6 {
    public static void main(String[] args) {
        int[][] matriz5x9 = new int[5][9];
        int[][] matriz9x5 = new int[9][5];

        // Llenar la primera matriz con valores aleatorios (por ejemplo, del 1 al 50)
        Random random = new Random();
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 9; j++) {
                matriz5x9[i][j] = random.nextInt(50) + 1;
            }
        }

        // Transponer la matriz 5x9 en la matriz 9x5
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 9; j++) {
                matriz9x5[j][i] = matriz5x9[i][j];
            }
        }

        // Mostrar la matriz original (5x9)
        System.out.println("Matriz 5x9:");
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 9; j++) {
                System.out.print(matriz5x9[i][j] + "\t");
            }
            System.out.println();
        }

        // Mostrar la matriz transpuesta (9x5)
        System.out.println("\nMatriz 9x5 (transpuesta):");
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 5; j++) {
                System.out.print(matriz9x5[i][j] + "\t");
            }
            System.out.println();
        }
    }
}