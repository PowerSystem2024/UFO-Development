package quizgame;

import java.util.Scanner;

public class CSS {
    public void startQuiz() {
        Scanner scanner = new Scanner(System.in);
        int respuestasCorrectas = 0;
        int respuestasIncorrectas = 0;

        System.out.print("Ingrese su nombre: ");
        String playerName = scanner.nextLine();

        System.out.println("\nTema: CSS - Responde las siguientes preguntas:");

        // Pregunta 1
        System.out.println("1. ¿Qué significa CSS?");
        System.out.println("a) Computer Style Sheets");
        System.out.println("b) Creative Style Sheets");
        System.out.println("c) Cascading Style Sheets");
        System.out.println("d) Colorful Style Sheets");
        System.out.print("Respuesta: ");
        String answer1 = scanner.next();
        if (answer1.equalsIgnoreCase("c")) {
            respuestasCorrectas++;
        } else {
            respuestasIncorrectas++;
        }

        // Pregunta 2
        System.out.println("2. ¿Qué propiedad de CSS se utiliza para cambiar el color de fondo?");
        System.out.println("a) background-color");
        System.out.println("b) color");
        System.out.println("c) bg-color");
        System.out.println("d) background");
        System.out.print("Respuesta: ");
        String answer2 = scanner.next();
        if (answer2.equalsIgnoreCase("a")) {
            respuestasCorrectas++;
        } else {
            respuestasIncorrectas++;
        }

        // Pregunta 3
        System.out.println("3. ¿Cuál de las siguientes opciones es una unidad de medida relativa en CSS?");
        System.out.println("a) px");
        System.out.println("b) cm");
        System.out.println("c) em");
        System.out.println("d) mm");
        System.out.print("Respuesta: ");
        String answer3 = scanner.next();
        if (answer3.equalsIgnoreCase("c")) {
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
