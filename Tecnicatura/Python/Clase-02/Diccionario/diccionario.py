#Un "Diccionario" esta compuesto por 2 elementos, una llave y un valor.
#dict(key,value)

diccionario = {
    "IDE": "Integrated Development Environment",
    "POO": "Programacion Orientada a Objetos",
    "SABD": "Sistema de Administracion de Bade de Datos"
}

tablaClientes = {
    'Nombre': 'InvValue',
    'Edad': 'number',
    'Direccion': 'String',
    'id': 1
}

print('')
print('Diccionario tablaClientes es: ',len(tablaClientes))
print('')
print(tablaClientes)
print('Longitud del diccionario tablaClientes')
print('')
print(len(tablaClientes))

print('')
print('Recorremos el diccionario')

for i in tablaClientes:
    print(i)

print('')
print(diccionario) #Muestro los elementos
print(len(diccionario)) #Muestra el numero de elmentos

print('')
#Acceder a un diccionario con la llave(key)
print(diccionario["IDE"]) #Muestra el valor de la llave

print('')
#Otra forma de obtener el valor de la llave
print(diccionario.get("POO")) #Obtenemos el valor de la llave con el metodo ".get()"

print('')
#Modificamos elementos
diccionario["IDE"] = "Entorno de Desarrollo Integrado" #Cambiamos el valor de la llave
print(diccionario)

print('')
print('Recorremos el diccionario con ciclo for')

print('')
print('in diccionario')
#Recorrer los elementos
for termino in diccionario: #Recorremos mostrando solo las llaves
    print(termino)

print('')
print('items')
#Necesitamos una funcion para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor) #Nos muestra las llaves y el valor

print('')
print('keys')
#Otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino) #Muestra solo las llaves con el metodo ".keys()"

print('')
print('values')
#Mostramos los valores sin las llaves
for valor in diccionario.values():
    print(valor) #Con el metodo ".value() solo accedemos al valor de las llaves"

print('')
#Comprobar la existencia de elementos
print("IDE" in diccionario) #Devuelve un booleano 

print('')
#Agregar un elemento 
diccionario["PK"] = "Primary Key"
print(diccionario)

print('')
print('Quitar un elemento del diccionario')
#Quitar un elemento
diccionario.pop("SABD") #Elimina la llave y su valor
print(diccionario)

print('')
#Vaciar un diccionario
diccionario.clear()
print(diccionario)

#Eliminar diccionario
# del diccionario


# Repaso de listas: para ordenar una lista desordenada se utiliza el metodo sort()
# Para poner una lista al reves se utiliza el metodo reverse()
# Para saber cuantos valores repetidos hay dentro de una lista se utiliza el metodo count(elemento). Esto cuenta
# cuantas veces aparece ese elemento dentro de la lista.

listaDeNumeros = [1, 4, 3, 6, 8, 10, 2, 12, 7, 9, 15, 18, 5, 11, 21, 25, 11, 20, 24, 23, 22]
print(listaDeNumeros.count(22))
print('')
listaDeNumeros.reverse()    # Esto da vuelta la lista, no la ordena al reves.
print(listaDeNumeros)
print('')
listaDeNumeros.sort()
print(listaDeNumeros)
print('')
print(listaDeNumeros.index(18))
