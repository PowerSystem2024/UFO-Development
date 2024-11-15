from Producto import Producto

class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self.id_orden = Orden.contador_ordenes
        self.productos = list(productos)

    def agregar_producto(self, producto):
        self.productos.append(producto) #   Esto es para agregar un nuevo producto

    def calcular_total(self):
        total = 0   # Variable temporal para almacenar el total temporal
        for producto in self.productos:
            total += producto.precio
        return total


    def __str__(self):
        productos_str = ''
        for producto in self.productos:
            productos_str += producto.__str__()+'|'
        return f'Orden:{self.id_orden},\nProducto:{productos_str}'


if __name__ == '__main__':
    producto1 = Producto('Camiseta',100.00)
    producto2 = Producto('Pantalon',150.00)
    producto3 = Producto('Campera',200.00)
    producto4 = Producto('camisa',125.00)
    productos1 = [producto1, producto2]
    productos2 = [producto3, producto4]
    orden1 = Orden(productos1)
    print(orden1)
    orden2= Orden(productos2)
    print(orden2)
