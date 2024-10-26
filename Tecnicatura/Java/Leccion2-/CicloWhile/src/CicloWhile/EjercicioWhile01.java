
package CicloWhile;


public class EjercicioWhile01 {
    public static void main(String[] args) {
        
        System.out.println("Ciclo While");
        var conteo = 0; // Inferencia de tipos
        while(conteo < 7){
            System.out.println("conteo = " + conteo);
            conteo ++;  // Incremento de 1 en 1
        }
        
        System.out.println("");
        System.out.println("Ciclo Do While");
        var contador = 0;
        do {
            System.out.println("contador = " + contador);
            contador ++;
        } while( contador < 7);
  }
}
