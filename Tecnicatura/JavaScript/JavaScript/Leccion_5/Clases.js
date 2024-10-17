//let persona3 = new Persona("Cele", "Pian"); esto no se debe hacer:

class Persona{ //Clase padre
    
    static contadorObjetosPersona = 0; //Atributo estatico
    //email = "Valor default email"; //Atributo no estatico

    static get MAX_OBJ(){// Este metodo simula una constante
        return 5;
    }

    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
        if(Persona.contadorObjetosPersona < Persona.MAX_OBJ){
            this.idPersona = ++Persona.contadorObjetosPersona;
        }
        else{
            console.log("Se ha superado el maximo de objeto permitidos");
        }
        
        //console.log("Se incrementa el contador: "+Persona.contadorObjetosPersona);
    }

    get nombre(){
        return this._nombre;
    }

    set nombre(nombre){
        this._nombre = nombre;
    }

    get apellido(){
        return this._apellido;
    }

    set apellido(apellido){
        this._apellido = apellido;
    }

    nombreCompleto(){
        return this.idPersona+" "+this._nombre+" "+this._apellido;
    }
    //Sobre escribiendo el metodo de la clase padre (Objet)
    toString(){ //Regresa un String
        //Se aplica el polimorfismo que significa = multiples formas en tiempos ejecucion
        //El metodo que se ejecuta depende si es una referencia de tipo padre o hija
        return this.nombreCompleto();
    }

    static saludar(){
        console.log("Saludos desde este metodo static");
    }

    static saludar2(persona){
        console.log(persona.nombre+" "+persona.apellido);
    }

}

class Empleado extends Persona{ //Clase hija
    constructor(nombre, apellido, departamento){
        super(nombre, apellido); 
        this._departamento = departamento;
    }

    get departamento(){
        return this._departamento;
    }

    set departamento(departamento){
        this._departamento = departamento;
    }

    //Sobreescritura
    nombreCompleto(){
        return super.nombreCompleto()+", "+this._departamento;
    }
}

let persona1 = new Persona("Mateo", "Pave");
console.log(persona1.nombre);
persona1.nombre = "Juaco Cion";
console.log(persona1.nombre);
//console.log(persona1);
let persona2 = new Persona("Cesar", "Lince");
console.log(persona2.nombre);
persona2.nombre = "Maria Lali";
console.log(persona2.nombre);
//console.log(persona2);

let empleado1 = new Empleado("Morena", "Gimena", "Sistema");
console.log(empleado1);
console.log(empleado1.nombreCompleto());

//Object.prototype.toString Esta es la manera de acceder a atributos y metodos de manera dinamica
console.log(empleado1.toString());
console.log(persona1.toString());

//persona1.saludar(); nose utiliza desde el objeto
Persona.saludar();
Persona.saludar2(persona1);

Empleado.saludar();
Empleado.saludar2(empleado1);

//console.log(persona1.contadorObjetosPersona);
console.log(Persona.contadorObjetosPersona);
console.log(Empleado.contadorObjetosPersona);

console.log(persona1.email);
console.log(empleado1.email);
//console.log(Persona.email); No puede acceder desde la clase
console.log(persona1.toString());
console.log(persona2.toString());
console.log(empleado1.toString());
console.log(Persona.contadorObjetosPersona);
let persona3 = new Persona("Coti", "Pame");
console.log(persona3.toString());
console.log(Persona.contadorObjetosPersona);

console.log(Persona.MAX_OBJ);
//Persona.MAX_OBJ = 10; // No se puede modificar, ni alterar
console.log(Persona.MAX_OBJ);

let persona4 = new Persona("Fran", "Doc");
console.log(persona4.toString());
let persona5 = new Persona("Lila", "Pave");
console.log(persona5.toString());