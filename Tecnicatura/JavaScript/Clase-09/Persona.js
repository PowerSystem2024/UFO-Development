class Persona {
  static contadorPersonas = 0;
  #idPersona;
  #nombre;
  #apellido;
  #edad;
  constructor(nombre, apellido, edad) {
    this.#idPersona = ++Persona.contadorPersonas;
    this.#nombre = nombre;
    this.#apellido = apellido;
    this.#edad = edad;
  }
  get idPersona() {
    return this.#idPersona;
  }
  get nombre() {
    return this.#nombre;
  }
  set nombre(nombre) {
    this.#nombre = nombre;
  }
  get apellido() {
    return this.#apellido;
  }
  set apellido(apellido) {
    this.#apellido = apellido;
  }
  get edad() {
    return this.#edad;
  }
  set edad(edad) {
    this.#edad = edad;
  }
  toString() {
    return `Persona[idPersona: ${this.#idPersona}, nombre: ${
      this.#nombre
    }, apellido: ${this.#apellido}, edad: ${this.#edad} ]`;
  }
}

let persona1 = new Persona("Monica", "Geller", 50);
console.log(persona1.toString());
