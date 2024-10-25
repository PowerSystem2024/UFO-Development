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

# MAS SOBRE LISTAS CONSULTANDO A CHAT GPT

# lAS LISTAS SE CREAN UTILIZANDO [] Y PUEDEN CONTENER CUALQUIER TIPO DE DATO. eJ

# Lista vacia
mi_lista = []

# Lista con diferentes tipos de datos
mi_lista = [1, 2, 3, 'Python', True, 3.14]

# ACCESO A ELEMNTOS DE LA LISTA
# Los elementos de la lista se acceden usando índices,
# comenzando desde 0:
mi_lista = ['a', 'b', 'c', 'd']
print(mi_lista[0])
print(mi_lista[3])
print(mi_lista[-1])

# SLICING O SEGMENTACIÓN
# El slicing permite obtener sublistas a partir de una lista principal
otra_nueva_lista = [0, 1, 2, 3, 4, 5]
print(otra_nueva_lista[1:4])
print(otra_nueva_lista[:3])
print(otra_nueva_lista[3:])
print(otra_nueva_lista[-3:])

# append()    agrega 1 elemento al final de la lista!
colores = ['rojo', 'azul', 'morado']
colores.append('blanco')
print(colores)
# Si intento agregar con append colocando entre ([]) ocurre
colores.append(['negro', 'amarillo'])
print(colores)


# extend([])    agrega multiples elementos al final de la lista!
provincias = ['Chaco', 'Corrientes', 'Catamarca', 'Jujuy']
provincias.extend(['Buenos Aires', 'Cordoba', 'Santa fe'])
print(provincias)
# NO OLVIDAR COLOCAR DENTRO DE [] 

# insert()  Inserta un elemento en un indice específico
marca_ropa = ['adidas', 'topper', 'nike']
marca_ropa.insert(1, 'kappa')
print(marca_ropa)