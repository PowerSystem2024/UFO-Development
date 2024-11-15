class Persona:
    contador_personas = 0#Variable de clase

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1 #vamos incrementando
        return cls.contador_personas

    def __init__(self, nombre, edad):
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona[{self.id_persona} {self.nombre} {self.edad}]'

persona1= Persona('Dario',41)
print(persona1)
persona2 = Persona('Pablo',35)
print(persona2)
persona3 = Persona('LilJosé',41)
print(persona3)
Persona.generar_siguiente_valor()
persona4= Persona('Victor',44)
print(persona4)
print(f'Valor contador persona : {Persona.contador_personas}')

# INCLUIMOS DESCRIPCIÓN ECHA CON LA AYUDA DE ChatGpt

# class Persona:
#     # Variable de clase: compartida por todas las instancias de la clase.
#     # Lleva un conteo global de las personas creadas.
#     contador_personas = 0

#     # Método de clase: usado para acceder o modificar atributos de clase.
#     # Este método incrementa el contador y devuelve su nuevo valor.
#     @classmethod
#     def generar_siguiente_valor(cls):
#         cls.contador_personas += 1  # Incrementa el contador global
#         return cls.contador_personas  # Devuelve el nuevo valor del contador

#     # Constructor: se ejecuta al crear una nueva instancia de la clase.
#     def __init__(self, nombre, edad):
#         # Se asigna un identificador único a la persona llamando al método de clase.
#         self.id_persona = Persona.generar_siguiente_valor()
#         # Inicializa los atributos 'nombre' y 'edad' con los valores proporcionados.
#         self.nombre = nombre
#         self.edad = edad

#     # Método especial: define cómo se representa una instancia como cadena.
#     # Esto se usa, por ejemplo, cuando se imprime una instancia con `print`.
#     def __str__(self):
#         return f'Persona[{self.id_persona} {self.nombre} {self.edad}]'

# # Creación de instancias de la clase Persona.
# # Cada instancia recibe un identificador único y se inicializa con nombre y edad.
# persona1 = Persona('Dario', 41)
# print(persona1)  # Salida: Persona[1 Dario 41]

# persona2 = Persona('Pablo', 35)
# print(persona2)  # Salida: Persona[2 Pablo 35]

# persona3 = Persona('LilJosé', 41)
# print(persona3)  # Salida: Persona[3 LilJosé 41]

# # Llamada directa al método de clase. Incrementa el contador global sin crear una nueva instancia.
# Persona.generar_siguiente_valor()

# # Se crea otra instancia de Persona.
# persona4 = Persona('Victor', 44)
# print(persona4)  # Salida: Persona[5 Victor 44]

# # Imprime el valor actual del contador global, reflejando todas las llamadas al método de clase.
# print(f'Valor contador persona : {Persona.contador_personas}')
# # Salida: Valor contador persona : 5

