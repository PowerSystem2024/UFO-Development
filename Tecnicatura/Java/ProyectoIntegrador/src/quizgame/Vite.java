package quizgame;

import java.util.Scanner;

public class Vite {
    public void startQuiz() {
        Scanner scanner = new Scanner(System.in);
        int respuestasCorrectas = 0;
        int respuestasIncorrectas = 0;

        System.out.print("Ingrese su nombre: ");
        String playerName = scanner.nextLine();

        System.out.println("\nTema: Vite - Responde las siguientes preguntas:");

        // Pregunta 1
        System.out.println("1. ¿Qué es Vite?");
        System.out.println("a) Un empaquetador de módulos");
        System.out.println("b) Un framework CSS");
        System.out.println("c) Un lenguaje de programación");
        System.out.println("d) Un navegador web");
        System.out.print("Respuesta: ");
        String answer1 = scanner.next();
        if (answer1.equalsIgnoreCase("a")) {
            respuestasCorrectas++;
        } else {
            respuestasIncorrectas++;
        }

        // Pregunta 2
        System.out.println("2. ¿Quién es el creador de Vite?");
        System.out.println("a) Evan You");
        System.out.println("b) Guido van Rossum");
        System.out.println("c) Ryan Dahl");
        System.out.println("d) Brendan Eich");
        System.out.print("Respuesta: ");
        String answer2 = scanner.next();
        if (answer2.equalsIgnoreCase("a")) {
            respuestasCorrectas++;
        } else {
            respuestasIncorrectas++;
        }

        // Pregunta 3
        System.out.println("3. ¿Cuál de las siguientes es una característica principal de Vite?");
        System.out.println("a) Carga lenta de módulos");
        System.out.println("b) Recarga en caliente ultra rápida");
        System.out.println("c) Emulación de bases de datos");
        System.out.println("d) Motor de renderizado");
        System.out.print("Respuesta: ");
        String answer3 = scanner.next();
        if (answer3.equalsIgnoreCase("b")) {
            respuestasCorrectas++;
        } else {
            respuestasIncorrectas++;
        }

        // Resultados
        System.out.println("\nResultados:");
        System.out.println("Respuestas correctas: " + respuestasCorrectas);
        System.out.println("Respuestas incorrectas: " + respuestasIncorrectas);

        // Guardar el puntaje en la tabla de líderes
        MainProgram.leaderboard.add(playerName + " - Puntaje: " + respuestasCorrectas + "/3");

        // Opciones para continuar
        System.out.println("\n1. Volver a jugar");
        System.out.println("2. Regresar al menú principal");
        System.out.print("Seleccione una opción: ");
        int choice = scanner.nextInt();

        if (choice == 1) {
            startQuiz();
        } else {
            System.out.println("Regresando al menú principal...");
        }
    }
}
