class Persona:
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs):
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni # Este atributo esta encapsulado de manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self):
        print(f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad} la direcciones: {self.args}, los datos importantes son: {self.kwargs}')

persona1 = Persona('Ariel', 'Betancud', 32445987, 40)
print(Persona)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}')

persona2 = Persona('Osvaldo', 'Giordanini', 22369852, 45)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
persona1.edad = 40
print(f'El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}')


#Los atributos son: caracteristicas
# Los metodos son: el comportamiento que van tener los objetos (acciones)

persona1.mostrar_detalle()
persona2.mostrar_detalle()

# Persona.mostrar_detalle(persona1) debemos pasarle una referencia para el self o dara error

persona1.telefono = '3624895511'
print(persona1.telefono)
print(f'Este es el telefono: {persona1.telefono}')
print(f'Este es el telefono de: {persona1.nombre} {persona1.telefono}')

#print(persona2.telefono) el objeto persona2 no tiene el atributo, da error

persona3 = Persona('Rogelio', 'Roma', 35987456, 22, 'Telefono', '26444557', 'Calle Lopez', 823, 'Manzana', 77, 'casa', 18, Altura=1.86, Peso=105, CFavorito='Azul', Modelo=2021)
persona3.mostrar_detalle()
#print(persona3._dni) esto no se debe utilizar en python
# persona3.__nombre Esta totalmente encapsulado  video 9