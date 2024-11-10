class Producto {
  static contadorProductos = 0;

  #idProducto;
  #nombre;
  #precio;

  constructor(nombre, precio) {
    this.#idProducto = ++Producto.contadorProductos;
    this.#nombre = nombre;
    this.#precio = precio;
  }

  get idProducto() {
    return this.#idProducto;
  }

  get nombre() {
    return this.#nombre;
  }

  set nombre(nombre) {
    this.#nombre = nombre;
  }

  get precio() {
    return this.#precio;
  }

  set precio(precio) {
    this.#precio = precio;
  }

  toString() {
    return `Producto: [idProducto: ${this.#idProducto}, nombre: ${
      this.#nombre
    }, precio: ${this.#precio}]`;
  }
}

class Orden {
  static contadorOrdenes = 0;
  static getMAX_PRODUCTOS() {
    return 5;
  }

  #idOrden;
  #productos;
  #contadorProductosAgregados;

  constructor() {
    this.#idOrden = ++Orden.contadorOrdenes;
    this.#productos = [];
    this.#contadorProductosAgregados = 0;
  }

  get idOrden() {
    return this.#idOrden;
  }

  agregarProducto(producto) {
    if (this.#productos.length < Orden.getMAX_PRODUCTOS()) {
      this.#productos.push(producto);
    } else {
      console.log(
        `No se pueden agregar más productos, ya se alcanzó el máximo que es ${Orden.getMAX_PRODUCTOS()}`
      );
    }
  }

  calcularTotal() {
    let totalVenta = 0;
    for (let producto of this.#productos) {
      totalVenta += producto.precio;
    }
    return totalVenta;
  }

  mostrarOrden() {
    let productosOrden = "";
    for (let producto of this.#productos) {
      productosOrden += producto.toString() + " ";
    }
    console.log(
      `Orden: ${
        this.#idOrden
      }, Total = $${this.calcularTotal()}, Productos: ${productosOrden}`
    );
  }
}

// ------------------------------- PRUEBA SISTEMA VENTAS ----------------------------
let producto1 = new Producto("Pantalon", 3000);
let producto2 = new Producto("Remera", 1500);
let producto3 = new Producto("Buzo", 2500);

let orden1 = new Orden();
orden1.agregarProducto(producto1);
orden1.agregarProducto(producto2);
orden1.agregarProducto(producto3);

orden1.mostrarOrden();
console.log("Total de la orden: " + orden1.calcularTotal());
