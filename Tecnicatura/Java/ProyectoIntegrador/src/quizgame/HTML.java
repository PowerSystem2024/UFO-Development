package quizgame;

import java.util.Scanner;

public class HTML {
    public void startQuiz() {
        Scanner scanner = new Scanner(System.in);
        int respuestasCorrectas = 0;
        int respuestasIncorrectas = 0;

        System.out.print("Ingrese su nombre: ");
        String playerName = scanner.nextLine();

        System.out.println("\nTema: HTML - Responde las siguientes preguntas:");

        // Pregunta 1
        System.out.println("1. ¿Qué significa HTML?");
        System.out.println("a) Hyper Text Markup Language");
        System.out.println("b) Home Tool Markup Language");
        System.out.println("c) Hyperlinks and Text Markup Language");
        System.out.println("d) Hyper Tool Multi Language");
        System.out.print("Respuesta: ");
        String answer1 = scanner.next();
        if (answer1.equalsIgnoreCase("a")) {
            respuestasCorrectas++;
        } else {
            respuestasIncorrectas++;
        }

        // Pregunta 2
        System.out.println("2. ¿Cuál es el elemento HTML utilizado para los títulos grandes?");
        System.out.println("a) <title>");
        System.out.println("b) <heading>");
        System.out.println("c) <h1>");
        System.out.println("d) <head>");
        System.out.print("Respuesta: ");
        String answer2 = scanner.next();
        if (answer2.equalsIgnoreCase("c")) {
            respuestasCorrectas++;
        } else {
            respuestasIncorrectas++;
        }

        // Pregunta 3
        System.out.println("3. ¿Qué etiqueta se usa para agregar un enlace en HTML?");
        System.out.println("a) <link>");
        System.out.println("b) <a>");
        System.out.println("c) <href>");
        System.out.println("d) <anchor>");
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
