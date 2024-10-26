
package CicloWhile;


public class EjercicioWhile01 {
    public static void main(String[] args) {
        
        System.out.println("");
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
        
        System.out.println("");
        System.out.println("Ciclo for");
        
        for( var contando = 0; contando < 7; contando++) {
            System.out.println("contando = " + contando);
        } // En el ciclo for si hace una sola linea de codigo, se puede
          // quitar las {} pero conviene dejarlas por buena práctica!
          
        
  }
}
