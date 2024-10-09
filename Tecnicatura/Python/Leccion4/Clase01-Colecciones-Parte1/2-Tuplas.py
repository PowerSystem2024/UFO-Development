# Definir una tupla
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(cocina)
print(len(cocina))

# Acceder a un elemento, para esto utilizaremos corchetes
print(cocina[0])
# Mostrar desde atras hacia adelante
print(cocina[-1])
# Como acceder a un rango
print(cocina[0:1])  # muestra ('cuchara') porque no incluye el final
print(cocina[0:2])  # muesrta ('cuchara', 'cuchillo')

# ACLARACIÓN: Tupla: un elemento entre parentesis seguido de al menos una coma
verduras = ('papa', )   #Es tupla
cajonDePapas = ('papas')    # Es una cadena

print('RECORREMOS LOS ELEMENTOS DE UNA TUPLA')
for cocinar in cocina:
    print(cocinar)      # Cada vez que la función print se ejecuta, hace un salto de linea, se llama \n

for cocinar in cocina:
    print(cocinar, end= ' ') # Con esta modificación le quitamos el salto de linea a la función print

# Las tuplas no son mutables, es decir, no se puede hacer cocina[1] = 'plato
# Para modificar una tupla, se hace la conversión a lista, luego se modifica y luego se convierte a tupla nuevamente

cocinaLista = list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print('\n', cocina)
