from Orden import Orden
from Producto import Producto

producto1 = Producto('Camiseta', 100.00)
producto2 = Producto('Pantalon', 150.00)
producto3 = Producto('Campera', 200.00)
producto4 = Producto('Camisa', 125.00)
producto6 = Producto('Medias', 25.00)
productos1 = [producto1, producto2]
productos2 = [producto3, producto4]
orden1 = Orden(productos1)
print(orden1)
print(f'Total de la orden1:{orden1.calcular_total()}')

orden2 = Orden(productos2)
orden2.agregar_producto(producto6)
orden2.agregar_producto(producto2)
print(orden2)
print(f'Total de la orden2:{orden2.calcular_total()}')