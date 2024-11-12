public class Ejercicio7 {
    public static void main(String[] args) {
        // Creación de una matriz 5x5
        int[][] matriz = new int[5][5];

        // Asignación de los bordes a 1
        for (int i = 0; i < 5; i++) {
            matriz[0][i] = 1; // Borde superior
            matriz[4][i] = 1; // Borde inferior
            matriz[i][0] = 1; // Borde izquierdo
            matriz[i][4] = 1; // Borde derecho
        }

        // Mostrar la matriz
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }
    }
}
