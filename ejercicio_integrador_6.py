#6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los  siguientes métodos para la clase: 
#• Un constructor, donde los datos pueden estar vacíos. 
#• Los setters y getters para cada uno de los atributos. Hay que validar las entradas de  datos. 
#• mostrar(): Muestra los datos de la persona. 
# es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad. 

class Persona:
    def __init__(self, nombre, edad, DNI):
        self.__nombre=nombre
        self.__edad=edad
        self.__DNI=DNI

    def __str__(self):
        return f"{self.__nombre}-{self.__edad}-{self.__DNI}"

    #Getters:
    @property
    def nombre(self):
        return f"Nombre: {self.__nombre}"

    @property
    def edad(self):
        return f"Edad: {self.__edad}"

    @property
    def DNI(self):
        return f"DNI: {self.__DNI}"

    #Setters:
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    @edad.setter
    def edad(self, nueva_edad):
        self.__edad =nueva_edad

    @DNI.setter
    def DNI(self, nuevo_DNI):
        self.__DNI =nuevo_DNI

    def mostrar1(self):
        print(f"Mi nombre es {self.__nombre}. Tengo {self.__edad} años. Mi DNI es {self.__DNI}")

    def es_mayor_de_edad(self):
        if self.__edad>=18:
            print(True)
        else: print(False)

'''
p1=Persona("Juan",15,32456978)
print(p1)
print(p1.nombre)
p1.mostrar1()
p1.es_mayor_de_edad()
p1.nombre="Ruperto"
p1.mostrar1()
p1.edad=24
p1.es_mayor_de_edad()
print(p1.edad)
p1.mostrar1()
p1.DNI=2556
p1.mostrar1()
'''