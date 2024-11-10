package quizgame;

import java.util.Scanner;

public class Vue {
    public void startQuiz() {
        Scanner scanner = new Scanner(System.in);
        int respuestasCorrectas = 0;
        int respuestasIncorrectas = 0;

        System.out.print("Ingrese su nombre: ");
        String playerName = scanner.nextLine();

        System.out.println("\nTema: Vue - Responde las siguientes preguntas:");

        // Pregunta 1
        System.out.println("1. ¿Quién es el creador de Vue?");
        System.out.println("a) Evan You");
        System.out.println("b) Brendan Eich");
        System.out.println("c) Guido van Rossum");
        System.out.println("d) Linus Torvalds");
        System.out.print("Respuesta: ");
        String answer1 = scanner.next();
        if (answer1.equalsIgnoreCase("a")) {
            respuestasCorrectas++;
        } else {
            respuestasIncorrectas++;
        }

        // Pregunta 2
        System.out.println("2. ¿Cuál de las siguientes características es una ventaja de Vue?");
        System.out.println("a) DOM Virtual");
        System.out.println("b) Data Binding bidireccional");
        System.out.println("c) Dependencias modulares");
        System.out.println("d) Todos los anteriores");
        System.out.print("Respuesta: ");
        String answer2 = scanner.next();
        if (answer2.equalsIgnoreCase("d")) {
            respuestasCorrectas++;
        } else {
            respuestasIncorrectas++;
        }

        // Pregunta 3
        System.out.println("3. ¿Qué se utiliza para definir la lógica y el estado en un componente Vue?");
        System.out.println("a) Metodologías CSS");
        System.out.println("b) Los mixins");
        System.out.println("c) El objeto de datos del componente");
        System.out.println("d) JSX");
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
