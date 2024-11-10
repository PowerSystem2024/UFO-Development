/*
let persona3 = new Persona("Roberto", "Lopez"); 
Esto no se puede hacer porque la clase Persona DEBE estar definida antes de ser utilizada: Persona is not defined
*/

class Persona {// Clase Padre
  
  constructor(nombre, apellido) {
    this._nombre = nombre; // Tener en cuenta que inicializamos con el _ para que no sea igual al del método get.
    this._apellido = apellido;
  }

  get nombre() {
    return this._nombre;
  }

  set nombre(nombre) {
    this._nombre = nombre;
  }

  get apellido() {
    return this._apellido; // Inicializamos el método get para apellido
  }

  set apellido(apellido) {
    this._apellido = apellido; // Inicializamos el método get para apellido
  }

  nombreCompleto() {
    //metodo para devolver el nombre.
    return this._nombre + " " + this._apellido; // Devolvemos el nombre y el apellido separado con un espacio.
  }

  //Sobreescribiendo el método de la clase padre (Object)
  toString() {
    //Devuelve un string
    //Se aplica polimorfismo (multiples formas en tiempo de ejecución)
    //El metodo que se ejeuta depende si es una referencia de tipo padre o hija
    return this.nombreCompleto();
  }
}

class Empleado extends Persona {// Clase Hija
  
  constructor(nombre, apellido, departamento) {
    //Tener en cuenta que hay que llamar al constructor de la clase padre y sus parámetros.
    super(nombre, apellido);
    this.departamento = departamento;
  }

  get departamento() {
    return this._departamento;
  }

  set departamento(departamento) {
    this._departamento = departamento;
  }

  //sobreescritura

  nombreCompleto() {
    return super.nombreCompleto() + " " + this._departamento;
  }
}

let persona1 = new Persona("Marcelo", "Polino");
console.log(persona1.nombre);
persona1.nombre = "Juan Angel";
console.log(persona1.nombre);
//console.log(persona1);
let persona2 = new Persona("Marcelo", "Tinelli");
console.log(persona2.nombre);
persona2.nombre = "Maria Luz";
console.log(persona2.nombre);
//console.log(persona2);

persona1.apellido = "Gonzalez"; //Mediante el set cambiamos el apellido y luego lo mostramos por consola.
console.log(persona1.apellido);

persona2.apellido = "Perez"; //Mediante el set cambiamos el apellido y luego lo mostramos por consola.
console.log(persona2.apellido);



let empleado1 = new Empleado("Pablo Jose", "Fachinoti", "Sistema");
console.log(empleado1); // Mostramos por consola el objeto empleado 1.
console.log(empleado1.nombre); // Mostramos solo el nombre del objeto empleado 1
console.log(empleado1.nombreCompleto());

//Object.prototype.toString Esta es la manera de acceder a atributos y métodos de manera dinamica
console.log(empleado1.toString());
console.log(persona1.toString());
