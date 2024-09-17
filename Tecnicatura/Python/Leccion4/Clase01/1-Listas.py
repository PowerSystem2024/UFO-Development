# VIDEO 1
lista = "Dario", "Carlos", "Zenon", "Luis", "Guille", "Jorge"
print(lista)
print(lista[3])
print(lista[-1])
print(lista[-2])
print(lista[-3])

print("")

nombres = ["Brenda", "Ariel", "Necus", "Guille", "Malevo"]
print(nombres[0])
print(nombres[-1])
print(nombres[-2])
print(nombres[-3])
print(nombres[0:2])
print(nombres[ :3])
print(nombres[1: ])

#VIDEO 2
# Modificar elementos en la lista
nombres[0] = "Liliana"
nombres[1] = "Brenda"
print(nombres)

# Iterar una lista
newlist = ["Pablo", "Checo", "Marcos", "Fernanda"]

for nombre in newlist: #nombre es una variable
    print(nombre)
else:
    print('Se acabaron los elementos de la lista!')

#VIDEO 3
# Preguntamos cuantos elementos tiene una lista
print(len(newlist))

#Agregar elemento a una lista usando el operador del punto
newlist.append('marcelo')
print(newlist)

#Insertar un elemento en un elemento específico
newlist.insert(1, 'Diego') #Los elementos se corren hacia la derecha para darle lugár al nuevo elemento.-
print(newlist)
newlist.insert(3, 'Debora')
print(newlist)

#Eliminar un elemento de la lista
newlist.remove('Checo')
print(newlist)

#Eliminar el último elemento
newlist.pop()
print(newlist)

#Eliminar un indice especifico
del newlist[2]
print(newlist)

#Limpiar toda la lista
newlist.clear()
print(newlist)

#Eliminar la lista
#del newlist
#print(newlist)  # Lo comentamos para evitar el error al ejecutar el código

print('Ejercicios: Uso de Rangos, antes de ver el video con la solución, debes intentar solucionarlo')
print('Continua en la carpeta 2-Ejercicios')