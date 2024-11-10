/*
let persona3 = new Persona("Roberto", "Lopez"); 
Esto no se puede hacer porque la clase Persona DEBE estar definida antes de ser utilizada: Persona is not defined
*/


class Persona{ // Clase Padre
  constructor(nombre, apellido){
      this._nombre = nombre; // Tener en cuenta que inicializamos con el _ para que no sea igual al del método get.
      this._apellido = apellido;
  } 

  get nombre(){
      return this._nombre;  
  }

  set nombre(nombre){
      this._nombre = nombre;
  }

  get apellido(){
      return this._apellido;  // Inicializamos el método get para apellido
  }

  set apellido(apellido){
      this._apellido = apellido; // Inicializamos el método get para apellido
  }  

}
class Empleado extends Persona{ // Clase Hija
    constructor(nombre, apellido, departamento){ //Tener en cuenta que hay que llamar al constructor de la clase padre y sus parámetros.
        super(nombre, apellido);
        this.departamento = departamento;
    }
    
    get departamento(){
        return this._departamento;
    }
  
    set departamento(departamento){
        this._departamento = departamento;
    }
  }

let persona1 = new Persona('Marcelo', 'Polino');
console.log(persona1.nombre);
persona1.nombre = "Juan Angel";
console.log(persona1.nombre)
//console.log(persona1);
let persona2 = new Persona('Marcelo', 'Tinelli');
console.log(persona2.nombre);
persona2.nombre = "Maria Luz";
console.log(persona2.nombre)
//console.log(persona2);

persona1.apellido = "Gonzalez";  //Mediante el set cambiamos el apellido a la persona1 y luego lo mostramos por consola.
console.log(persona1.apellido)

persona2.apellido = "Perez";      //Mediante el set cambiamos el apellido a la persona2 y luego lo mostramos por consola.
console.log(persona2.apellido)

let empleado1 = new Empleado('Pablo Jose', 'Fachinoti', 'Sistema');
console.log(empleado1); // Mostramos por consola el objeto empleado 1.
console.log(empleado1.nombre) // Mostramos solo el nombre del objeto empleado 1
console.log(empleado1._departamento)