package quizgame;

import java.util.Scanner;

public class Java {
    public void startQuiz() {
        Scanner scanner = new Scanner(System.in);
        int respuestasCorrectas = 0;
        int respuestasIncorrectas = 0;

        System.out.print("Ingrese su nombre: ");
        String playerName = scanner.nextLine();

        System.out.println("\nTema: Java - Responde las siguientes preguntas:");

        // Pregunta 1
        System.out.println("1. ¿Quién es conocido como el creador de Java?");
        System.out.println("a) James Gosling");
        System.out.println("b) Dennis Ritchie");
        System.out.println("c) Guido van Rossum");
        System.out.println("d) Bjarne Stroustrup");
        System.out.print("Respuesta: ");
        String answer1 = scanner.next();
        if (answer1.equalsIgnoreCase("a")) {
            respuestasCorrectas++;
        } else {
            respuestasIncorrectas++;
        }

        // Pregunta 2
        System.out.println("2. ¿Cuál es la extensión de archivos para programas en Java?");
        System.out.println("a) .js");
        System.out.println("b) .class");
        System.out.println("c) .java");
        System.out.println("d) .py");
        System.out.print("Respuesta: ");
        String answer2 = scanner.next();
        if (answer2.equalsIgnoreCase("c")) {
            respuestasCorrectas++;
        } else {
            respuestasIncorrectas++;
        }

        // Pregunta 3
        System.out.println("3. ¿Cuál de los siguientes es un concepto clave en Java?");
        System.out.println("a) Prototipos");
        System.out.println("b) Clases y objetos");
        System.out.println("c) Hojas de estilo");
        System.out.println("d) Scripts del servidor");
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
