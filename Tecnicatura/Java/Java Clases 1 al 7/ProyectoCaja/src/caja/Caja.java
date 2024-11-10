
package caja;//Package


public class Caja { //Clase Publica
    //Atributos (Caracreristicas)
    int ancho;
    int alto;
    int profundo;
    //Metodos y constructores (Acciones)
    public Caja(){ //Constructor 1 = vacio    
    }
    //Constructor con Parametros
    public Caja(int ancho, int alto, int profundo){ // Constructor 2
        this.ancho = ancho;
        this.alto = alto;
        this.profundo = profundo;
        
    }
    
    public int calcularVolumen(){
        return ancho * alto * profundo;
    }
            
    
}
