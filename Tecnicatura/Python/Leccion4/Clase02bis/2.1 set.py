# Colecciones del tipo set
# La lista mantiene un orden y se puede modifica, esto quiere decir que es mutable
# La tupla mantiene un orden y no se puede modificar, esto hace que la veamos como inmutable
# Set en cambio, no tiene un orden y no permite almacenar elementos duplicados o repetidos
# este no se puede modificar pero si se puede agregar o eliminar, es decir, no es completamente mutable o inmutable
# Un elemento del tipo set es una colección sin orden y sin indices.- {ES PARECIDO A UN DICCIONARIO, PERO AQUÍ NO HAY PARES codigo:valor}
# Al tipo set tambien se lo conoce como conjunto

# Creamos un set de planetas
planetas = {'Marte', 'Júpiter', 'Venus'}
print(len(planetas))        # La funcion len nos dice el largo que hay, en este caso es 3

# Revisar si un elemento existe dentro del set
print('Marte' in planetas)      # Preguntamos si Marte está en planetas
print('luna' in planetas)       # Preguntamos si luna está en planetas
print('Venus' not in planetas)  # Preguntamos si venus no está en planetas

# Agregar un elemento
planetas.add('Tierra')
print(planetas)

# La colección de tipo set nos puede servir para evitar elementos duplicados en una lista de datos, dni, nombre y apellido de una persona, matriula de un vehículo, etc
# entonces, poner esos datos en una lista de tipo set o en un conjunto nos va a facilitar las cosas porque sabemos que nunca se van a duplicar.

# Eliminar un elemento, puede arrojar un error si el elemento no existe!

planetas.remove('Júpiter')  # SI NO PUSIERA EL ASENTO ME DARÍA UN ERROR!
print(planetas)
planetas.discard('tierra')  # Con esta funcion discadr podemos eliminar y no nos da error, pero no elimina!
print(planetas)
planetas.discard('Tierra')
print(planetas)

# Limpiar set
planetas.clear()
print(planetas)

