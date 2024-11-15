# Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuacion elimine los elementos repetidos
# Mostrar la lista

#Creamos la lista
lista = [1, 2, 2, 3, 4, 4, 5, "Leandro", 1, 2, 2, 3, 4, 4, 5, "Leandro"]
# a continuación convertimos la lista a tipo set(conjunto) ya que un conjunto de este tipo no almacena elementos
# repetidos.
lista = list(set(lista)) # Convertimos la lista a un conjunto de tipo "set"
print(lista) #Mostramos la lista
# se convierte la lista a tipo set y luego se convierte en tipo lista nuevamente en un solo paso, 
# es por eso que englobamos con list a todo el parentesis en donde convertimos la lista a un tipo set