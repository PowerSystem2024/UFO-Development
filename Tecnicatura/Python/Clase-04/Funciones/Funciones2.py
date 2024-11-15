print('FUNCION SIN PARAMETROS')
print('')

def saludar():
    print('Hola!, bienvenido a Python')

# Llamamos a la funcion.
saludar()

print('FUNCION CON PARAMETROS')
print('')

def saludarPersona(nombre): # NO OLVIDAR QUE EL PARAMETRO QUE VA A RECIBIR ES UN STRING
    print(f'Hola, como estas {nombre}')

# Llamamos a la función.
saludarPersona('Dario')

# PODEMOS INGRESAR UN NOMBRE PARA QUE RECIBA EL PARAMETRO POR TECLADO

print('')
nombreDelSeñor = input('Buenos días, ingresa tu nombre: ')
def saludarSeñor(nombreDelSeñor):
    print(f'Hola, como te encuentras hoy {nombreDelSeñor}')

# LLAMAMOS A LA FUNCIÓN PARA QUE SALUDE LUEGO DE QUE EL PROGRAMA YA LE PIDIO AL USUARIO QUE INGRESE SU NOMBRE
saludarSeñor(nombreDelSeñor)

print('FUNCION CON MULTIPLES PARAMETROS')
print('')

# VAMOS A INGRESAR POR TECLADO LOS NUMEROS A SUMAR
a = int(input('Ingrese el primer número a sumar: '))
b = int(input('Ingrese el segundo número a sumar: '))
c = int(input('Ingrese el tercer número a sumar: '))
d = int(input('Ingrese el cuarto número a sumar: '))
def sumarNumeros(a,b,c,d):
    return a+b+c+d

# Llamamos a la función para que se ejecute pero como es una función que retorna un valor, devemos ponerla dentro de un print para que se pueda ver el resultado.

print(f'La suma de los números ingresados es: {sumarNumeros(a,b,c,d)}')
