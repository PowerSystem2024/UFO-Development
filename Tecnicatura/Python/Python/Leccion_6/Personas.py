class Persona: # Creamos una clase
   
   def __init__(self, nombre, apellido, dni, edad, *args, **kwargs): # Se lo llama metodo Init Dunder
       self.nombre = nombre
       self.apellido = apellido
       self._dni = dni # Este atributo esta encapsulado de una manera sugerida
       self.edad = edad
       self.args = args
       self.wkargs = kwargs
       
   def mostrar_detalle(self): # self es igual a this
       print(f"La clase Persona tiene los siguientes datos : {self.nombre} {self.apellido} {self._dni} {self.edad}, la direccion es: {self.args}, los datos importantes son: {self.wkargs}")
       
       
persona1 = Persona("Valentin", "Herrera", 1011121314, 18) # Necisitamos enviar argumentos
# print(persona1.nombre) # Tarea: Hacer el print igual que con el objeto
# print(persona1.apellido)
# print(persona1.edad)
print(f"El objeto 1 de la clase persona: {persona1.nombre} {persona1.apellido} su edad es: {persona1.edad}")
persona2 = Persona("Lucas", "Castro", 987654321, 19)
print(f"El objeto 2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}")

persona1.nombre = "Laura"
persona1.apellido = "Bentra"
persona1.edad = 20
print(f"El objeto 1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} su edad es: {persona1.edad}")

# Los atributos son: caracteristicas
# Los metodos son: el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle() # La referencia en este caso se pasa de manera automatica
persona2.mostrar_detalle()

# Persona.mostrar_detalle(persona1) # Debemos pasarle una referencia para el self o dara error
persona1.telefono = "123456789"
print(f"Este es el telefono: {persona1.nombre} {persona1.telefono}") # Hemos creado un atributo de un objeto

#print(persona2.telefono) el objeto persona2 no tiene este atributo, da error
persona3 = Persona("Rodrigo", "Roma", 135798642, 20, "Telefono", "123456789", "Calle Lilo", 321, "Manzana", 77, "Casa", 18, Altura=1.75, Peso=100, CFavorito="Negro", Auto="Toyota", Modelo=2023)
persona3.mostrar_detalle()
# print(persona3._dni) # Esto no se debe utilizar(esta encapsulado), esto dice que lo desconocido
# persona3.__nombre # Esta totalmente encapsulado
