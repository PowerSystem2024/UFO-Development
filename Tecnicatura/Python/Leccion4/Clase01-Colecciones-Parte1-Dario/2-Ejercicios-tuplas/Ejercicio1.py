# Dada la siguiente tupla,
tupla = (13, 1, 8, 3, 2, 5, 8)  # Se define la tupla
# Crear una lista que solo incluya los números menores a 5 e imprima por consola [1, 3, 2]

nuevaLista = list(tupla)    # Paso la tupla a una lista
print(nuevaLista)           # Imprimo la lista y ya puedo ver el resultado entre []

print('')

for i in nuevaLista:        # hago una prueba recorriendo la lista con un bucle for i
    print(i)                

print('')


resultado = []
for i in nuevaLista:        #imprimo los numeros del 1 al 3 recorriendo con un condicional
    if i < 5:
        resultado.append(i)

print(resultado)

