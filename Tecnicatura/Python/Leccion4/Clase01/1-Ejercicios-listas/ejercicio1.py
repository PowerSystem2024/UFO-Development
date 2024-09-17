print('iterar un rango de 0 a 10 e inprimir números divisibles entre 3')

array = []
for i in range(10):         # i es la variable y el rango 10 es el total de valores
    if i % 3 == 0:          # valores divisibles entre 3
        array.append(i)     # agregar al final del array
print(array)                # imprimir el array imprime [0, 3, 6, 9]