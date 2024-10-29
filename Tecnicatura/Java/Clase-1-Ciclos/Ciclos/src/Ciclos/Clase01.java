
package Ciclos;

/**
 *
 * @author Dario B.
 */
public class Clase01 {
    public static void main(String[] args) {
        
        System.out.println("");
        System.out.println("Ciclo while");
        
        var contador = 0;   // inferencia de tipos con var
        while (contador < 7) {
            System.out.println("Contador = " + contador);
            contador ++;
        }
        
        System.out.println("");
        System.out.println("Ciclo do while");
        
        var conteo = 0;
        do {
            System.out.println("conteo = " + conteo);
            conteo ++;
        } while ( conteo < 7);
        
        System.out.println("");
        System.out.println("Ciclo for");
        
        for ( var contando = 0; contando < 7; contando ++ ) {
            System.out.println("contando = " + contando);
        }
        
        //  Recordando el tipo de progr. goto!!!
        //  No recomendable usar!
        System.out.println("");
        System.out.println("Ciclo for con break");
        
        for ( var cont = 0; cont < 7 ; cont ++ ) {
            if (cont % 2 == 0) {
                System.out.println("cont = " + cont);
                break;
            }
        }

        System.out.println("");
        System.out.println("Ciclo for con continue");
        
        for ( var count = 0; count < 7 ; count ++ ) {
            if (count % 2 != 0) {
                continue;  
            }
            System.out.println("cont = " + count);
        }
        
        System.out.println("");
        System.out.println("Uso de etiquetas Labeks");
        
        // con break
        inicio:
        for ( var contando = 0; contando < 7 ; contando ++ ) {
            if (contando % 2 == 0) {
                System.out.println("contando = " + contando);
                break inicio;
            }
        }
        
        // con inicio
        inicio:
        for ( var count = 0; count < 7 ; count ++ ) {
            if (count % 2 != 0) {
                continue inicio;  
            }
            System.out.println("cont = " + count);
        }
        
    }
    
}
