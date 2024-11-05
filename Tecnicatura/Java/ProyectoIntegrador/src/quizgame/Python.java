package quizgame;

import java.util.Scanner;

public class Python {
    public void startQuiz() {
        Scanner scanner = new Scanner(System.in);
        int respuestasCorrectas = 0;
        int respuestasIncorrectas = 0;

        System.out.print("Ingrese su nombre: ");
        String playerName = scanner.nextLine();

        System.out.println("\nTema: Python - Responde las siguientes preguntas:");

        // Pregunta 1
        System.out.println("1. ¿Qué es Python?");
        System.out.println("a) Un lenguaje de programación");
        System.out.println("b) Un sistema operativo");
        System.out.println("c) Un navegador web");
        System.out.println("d) Un editor de texto");
        System.out.print("Respuesta: ");
        String answer1 = scanner.next();
        if (answer1.equalsIgnoreCase("a")) {
            respuestasCorrectas++;
        } else {
            respuestasIncorrectas++;
        }

        // Pregunta 2
        System.out.println("2. ¿Quién creó Python?");
        System.out.println("a) James Gosling");
        System.out.println("b) Guido van Rossum");
        System.out.println("c) Brendan Eich");
        System.out.println("d) Tim Berners-Lee");
        System.out.print("Respuesta: ");
        String answer2 = scanner.next();
        if (answer2.equalsIgnoreCase("b")) {
            respuestasCorrectas++;
        } else {
            respuestasIncorrectas++;
        }

        // Pregunta 3
        System.out.println("3. ¿Cuál es la extensión de archivos para Python?");
        System.out.println("a) .java");
        System.out.println("b) .py");
        System.out.println("c) .html");
        System.out.println("d) .css");
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
            // No llamar a MainProgram.main(null), simplemente regresa al menú principal
        }
    }
}
