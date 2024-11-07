class Empleado extends Persona {
  static contadorEmpleados = 0;
  #idEmpleado;
  #sueldo;
  constructor(nombre, apellido, edad, sueldo) {
    super(nombre, apellido, edad);
    this.#idEmpleado = ++Empleado.contadorEmpleados;
    this.#sueldo = sueldo;
  }
  get idEmpleado() {
    return this.#idEmpleado;
  }
  get sueldo() {
    return this.#sueldo;
  }
  set sueldo(sueldo) {
    this.#sueldo = sueldo;
  }
  toString() {
    return (
      super.toString() +
      " " +
      `Empleado[idEmpleado: ${this.#idEmpleado}, sueldo: $${this.#sueldo}]`
    );
  }
}
