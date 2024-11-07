class Cliente extends Persona {
  static contadorClientes = 0;
  #idCliente;
  #fechaRegistro;
  constructor(nombre, apellido, edad, fechaRegistro) {
    super(nombre, apellido, edad);
    this.#idCliente = ++Cliente.contadorClientes;
    this.#fechaRegistro = fechaRegistro;
  }
  get idCliente() {
    return this.#idCliente;
  }
  get fechaRegistro() {
    return this.#fechaRegistro;
  }
  set fechaRegistro(fechaRegistro) {
    this.#fechaRegistro = fechaRegistro;
  }
  toString() {
    return (
      super.toString() +
      `Cliente[idCliente: ${this.#idCliente}, fechaRegistro: ${
        this.#fechaRegistro
      }]`
    );
  }
}
