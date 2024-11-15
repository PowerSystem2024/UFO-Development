class Persona:
    def __init__(self, nombre,apellido,dni,edad, *args, **kwargs): 
        self.__nombre = nombre
        self.apellido = apellido
        self._dni = dni 
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self):
        print(f'La clase Persona tiene los siguientes datos: {self.__nombre} {self.apellido} {self._dni} {self.edad}, la direccion es: {self.args}, los otros datos importantes son: {self.kwargs}')

persona1 = Persona('Dario','Benitez',29934398, 40)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

print(f'El objeto 1 de la clase persona es: {persona1.nombre} {persona1.apellido}, su ead es: {persona1.edad}')

persona2 = Persona('Horacio','Benitez',13320494, 65)
print(f'El objeto 2 de la clase persona es: {persona2.nombre} {persona2.apellido}, su ead es: {persona2.edad}')

persona1.nombre = 'Rocio'
persona1.apellido = 'Benitez'
persona1.edad=40
print(f'El objeto 1 modificado de la clase persona es: {persona1.nombre} {persona1.apellido}, su ead es: {persona1.edad}')


persona1.mostrar_detalle() 
persona2.mostrar_detalle()

#Persona.mostrar_detalle(persona1) # Debemos pasarle una referencia para el self o dara error

persona1.telefono = '421187' # Creamos un atributo de un objeto, el cual es solopara el objeto persona1
print(f'Este es el telefono de: {persona1.nombre} {persona1.telefono}')

persona3 = Persona('Andres', 'Stacul',325154, 22,'Telefono','17422190','Calle bogio', 85,'Manzana',11,'Casa',25, Altura=1.87, Peso= 89,CFavorito='Azul',Auto='VW Gol',Modelo=2017)
persona3.mostrar_detalle()
print(persona3._dni) 
