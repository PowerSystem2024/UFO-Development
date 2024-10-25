# LO VISTO ANTERIORMENTE PERTENECEN A COLECCIONES EN PYTHON
# LAS LISTAS SE CONOCEN TAMBIEN COMO ARREGLOS
# LAS LISTAS PUEDEN CONTENER DISTINTOS TIPOS DE DATOS
print('Lista con diferentes tipos de datos')
datosComputacionales = ['Ram', 255, True, False, 'Byte', 0.3511]
print(datosComputacionales)

print('*')
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
listaConcat = lista1 + lista2
print(listaConcat)

lista2.extend([7, 8, 9, 10])
listaExtendida = lista1 + lista2
print(listaExtendida)

# INDEX
#Para ver el índice en el que está un elemento
print(listaExtendida.index(7))

# COUNTS
# cuenta cuantos valores repetidos hay dentro de una lista

revisar = [1, 2, 3, 3, 3, 3, 5, 8, 4, True, True, 'str', 'Example']
print(revisar.count(True)) # muestra 3. El Nº1 es tratado como un valor True en python.

# REVERTIR UNA LISTA.
revisar.reverse()
print(revisar)

#MULTIPLICAR UNA LISTA REPITIENDO SUS ELEMENTOS
listaMulti2 = [1, 2, 3] * 2
print(listaMulti2) # imprime [1, 2, 3, 1, 2, 3]
listaMulti3 = ['a', 'b', 'c', 'd', 'e']
print(listaMulti3 * 3)

# METODD SORT Para ordenar listas de manera ascendente
ordename = [1, 5, 7, 3, 9, 15, 0, 3, 4, 2]
print(ordename)
ordename.sort()
print(ordename)

# DAR VUELA UNA LISTA
ordename.sort(reverse = True)
print(ordename)

# RESUMEN LISTAS
# PUEDEN CONTENER DIFERENTE TIPO DE DATOS
# PUEDEN CONCATENARSE DOS O MAS LISTAS