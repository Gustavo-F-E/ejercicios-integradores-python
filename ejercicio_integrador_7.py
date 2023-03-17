#7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una  persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es  opcional. Crear los siguientes métodos para la clase: 
#• Un constructor, donde los datos pueden estar vacíos. 
#• Los setters y getters para cada uno de los atributos. El atributo no se puede modificar  directamente, sólo ingresando o retirando dinero. 
#• mostrar(): Muestra los datos de la cuenta. 
#• ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es  negativa, no se hará nada. 
#• retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números  rojos.

from ejercicio_integrador_6 import Persona

class Cuenta(Persona):
    def __init__(self, nombre, edad, DNI, titular, cantidad=0):
        super().__init__(nombre, edad, DNI)
        self.__titular=titular
        self.__cantidad=cantidad
    
    def __str__(self):
        return super().__str__()+f"-{self.__titular}-{self.__cantidad}"

    #Getters:
    @property
    def titular(self):
        return self.__titular

    @property
    def cantidad(self):
        return self.__cantidad

    #Setters:
    @titular.setter #El titular de la cuenta puede ser una persona diferente a la persona ingresada
    def titular(self, nuevo_titular):
        self.__titular = nuevo_titular
    
    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        self.__cantidad = nueva_cantidad

    def mostrar2(self):
        print(f"El titular de la cuenta es  {self.__titular} y su saldo es ${self.__cantidad}")

    def ingresar(self, cantidad):
        if cantidad>=0:
            saldo_ingresar=cantidad
            print(f"{self.__titular} ingresa ${saldo_ingresar}")
            self.__cantidad+=cantidad
            print(f"El titular de la cuenta es  {self.__titular} y su saldo es ${self.__cantidad}")

    def retirar(self, cantidad):
        if cantidad>0:
            saldo_retirar=cantidad
            print(f"{self.__titular} retira ${saldo_retirar}")
            self.__cantidad-=cantidad
            print(f"El titular de la cuenta es  {self.__titular} y su saldo es ${self.__cantidad}")

'''
c1=Cuenta("Juan", 20,32456789,"Juan",15000)
print(c1)
c1.ingresar(1000)
c1.retirar(50000)
'''