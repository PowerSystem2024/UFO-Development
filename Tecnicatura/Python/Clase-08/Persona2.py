class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property 
    def nombre(self): 
        print('Estamos utilizando el metodo get')
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        print('Estamos utilizando el metodo set')
        self._nombre = nombre

    @property   
    def apellido(self):  
        print('Estamos utilizando el metodo get')
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):  
        print('Estamos utilizando el metodo set')
        self._apellido = apellido

    @property  
    def edad(self):  
        print('Estamos utilizando el metodo get')
        return self._edad

    @edad.setter
    def edad(self, edad):  
        print('Estamos utilizando el metodo set')
        self._edad = edad

    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad}')

if __name__ == '__main__':
    persona1 = Persona2('Esteban', 'CUttro',21)
    print(persona1.nombre) 
    print(persona1.apellido)
    print(persona1.edad)
    print('')

    persona1.nombre = 'Juan Parceliere' 
    print(persona1.nombre)
    print(persona1.mostrar_detalles())
    
    print('')
    persona2 = Persona2('Nat','Benit',43)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    persona2.nombre = 'Natalia'
    persona2.apellido = 'Benitez'
    persona2.edad = 22

    print('')
    print(persona2.mostrar_detalles())

    persona3 = Persona2('Ester','Per',21)
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    persona3.nombre = 'Ester'
    persona3.apellido = 'Perez'
    persona3.edad = 31

    print(persona3.mostrar_detalles())
    
    print('')
    persona4 = Persona2('Cati','Rom', 35)
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    persona4.nombre = 'Catalina'
    persona4.apellido = 'Romero'
    persona4.edad = 28
    
    print('')
    print(persona4.mostrar_detalles())

    print(__name__)

    # COMENTARIOS

# Este código define la clase `Persona2`, que representa a una persona con tres atributos privados:
# nombre, apellido y edad. Estos atributos se inicializan en el constructor `__init__` cuando se crea una instancia de la clase.

# El método `mostrar_detalles` imprime los datos de la persona en un formato descriptivo.
# La clase utiliza propiedades (`@property`) para implementar métodos *getter* y *setter* para cada atributo.
# Los decoradores `@property` permiten acceder y modificar los valores de forma controlada y sencilla, ya que permiten acceder a los atributos como si fueran propiedades públicas, pero en realidad se utilizan métodos para mayor control.

# Cada propiedad (`nombre`, `apellido` y `edad`) cuenta con un método *getter* y un método *setter*.
# El *getter* devuelve el valor del atributo, mientras que el *setter* permite modificarlo.
# Esto se hace sin que el usuario tenga que invocar explícitamente métodos, lo que mantiene la sintaxis limpia y clara.

# El método `__del__` se llama automáticamente cuando se elimina una instancia de la clase `Persona2`.
# Este método imprime un mensaje indicando que la instancia ha sido eliminada junto con los valores de los atributos, lo cual puede ser útil para depuración.

# En el bloque `if __name__ == '__main__':`, se crean instancias de `Persona2` (`persona1` a `persona4`), para probar la funcionalidad de la clase.
# En cada caso, se utilizan los métodos *getter* para ver los valores iniciales de los atributos y luego los métodos
