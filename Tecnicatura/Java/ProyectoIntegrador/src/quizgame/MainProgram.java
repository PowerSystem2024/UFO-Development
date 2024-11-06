package quizgame;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class MainProgram {
    static List<String> leaderboard = new ArrayList<>(); // Lista para almacenar puntajes de jugadores

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            boolean exit = false;
            
            while (!exit) {
                System.out.println("\u001B[32m" + "+------------------------------------+");
                System.out.println("\u001B[32m" + "|                                    |");
                System.out.println("\u001B[32m" + "|        BIENVENIDOS SOMOS UFO       | ");
                System.out.println("\u001B[32m" + "|            DEVELOPMENT             | ");
                System.out.println("\u001B[32m" + "|                                    | ");
                System.out.println("\u001B[32m" + "+------------------------------------+");
                System.out.println("\u001B[32m" + "|  Bienvenido al juego de preguntas  | ");
                System.out.println("\u001B[32m" + "|  donde aprenderás jugando, los     | ");
                System.out.println("\u001B[32m" + "|  conceptos fundamentales en        | ");
                System.out.println("\u001B[32m" + "|  programación.                     | ");
                System.out.println("\u001B[32m" + "|                                    | ");
                System.out.println("\u001B[32m" + "+------------------------------------+");
                System.out.println("\u001B[32m" + "|            Menú Principal          | ");
                System.out.println("\u001B[32m" + "+------------------------------------+");
                System.out.println("\u001B[32m" + "|  1. Jugar                          | ");
                System.out.println("\u001B[32m" + "|  2. Ver mejores jugadores          | ");
                System.out.println("\u001B[32m" + "|  3. Salir                          | ");
                System.out.println("\u001B[32m" + "+------------------------------------+" + "\u001B[0m");
                System.out.print("Seleccione una opción: ");
                
                int choice;
                choice = Integer.parseInt(scanner.nextLine());
                
                switch (choice) {
                    case 1 -> playGame();
                    case 2 -> mostrarMejoresJugadores();
                    case 3 -> {
                        System.out.println("\u001B[32m" + "+-----------------------------------------------+");
                        System.out.println("\u001B[32m" + "| ¡Gracias por haber jugado!                    |");
                        System.out.println("\u001B[32m" + "| Nos despedimos desde UFO-Development,         |");
                        System.out.println("\u001B[32m" + "| de la Tecnicatura en Programación de          |");
                        System.out.println("\u001B[32m" + "| la Universidad Tecnológica de San             |");
                        System.out.println("\u001B[32m" + "| Rafael, Mendoza. ¡Esperamos verte pronto      |");
                        System.out.println("\u001B[32m" + "| y que sigas aprendiendo con nosotros!         |");
                        System.out.println("\u001B[32m" + "+-----------------------------------------------+" + "\u001B[0m");
                        exit = true;
                    }
                    default -> System.out.println("Opción inválida. Intente de nuevo.");
                }
            }
        }
    }

    private static void playGame() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("\u001B[32m" + "+-------------------------------------+");
        System.out.println("\u001B[32m" + "|        Elige tu tema de interés     |");
        System.out.println("\u001B[32m" + "+-------------------------------------+");
        System.out.println("\u001B[32m" + "|  1: Python                          |");
        System.out.println("\u001B[32m" + "|  2: Java                            |");
        System.out.println("\u001B[32m" + "|  3: JavaScript                      |");
        System.out.println("\u001B[32m" + "|  4: HTML                            |");
        System.out.println("\u001B[32m" + "|  5: CSS                             |");
        System.out.println("\u001B[32m" + "|  6: Vue                             |");
        System.out.println("\u001B[32m" + "+-------------------------------------+" + "\u001B[0m");
        System.out.print("Seleccione un tema: ");
        int topicChoice = scanner.nextInt();

        switch (topicChoice) {
            case 1 -> {
                Python python = new Python();
                python.startQuiz();
            }
            case 2 -> {
                Java java = new Java();
                java.startQuiz();
            }
            
            default -> System.out.println("Tema no disponible. Seleccione una opción válida.");
        }

        // Aquí puedes añadir otros casos para cada tema
            }

    public static void mostrarMejoresJugadores() {
        System.out.println("\u001B[32m" + "+-------------------------------------+");
        System.out.println("\u001B[32m" + "|      Tabla de Mejores Jugadores     |");
        System.out.println("\u001B[32m" + "+-------------------------------------+");
        if (leaderboard.isEmpty()) {
            System.out.println("\u001B[32m" + "|      No hay puntajes registrados.   |");
        } else {
            for (String entry : leaderboard) {
                System.out.println("|  " + entry);
            }
        }
        System.out.println("\u001B[32m" + "+-------------------------------------+" + "\u001B[0m");
    }
}
