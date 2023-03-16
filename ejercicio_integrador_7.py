#7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una  persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es  opcional. Crear los siguientes métodos para la clase: 
#• Un constructor, donde los datos pueden estar vacíos. 
#• Los setters y getters para cada uno de los atributos. El atributo no se puede modificar  directamente, sólo ingresando o retirando dinero. 
#• mostrar(): Muestra los datos de la cuenta. 
#• ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es  negativa, no se hará nada. 
#• retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números  rojos.

class Cuenta:
    def __init__(self, titular, cantidad):
        self.__titular=titular
        self.__cantidad=cantidad

    #Getters:
    @property
    def titular(self):
        return self.__titular

    @property
    def cantidad(self):
        return self.__cantidad

    #Setters:
    @titular.setter
    def titular(self, nuevo_titular):
        self.__titular = nuevo_titular
    
    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        self.__cantidad = nueva_cantidad

    def mostrar(self):
        print(f"El titular de la cuenta es  {self.__titular} y su saldo es {self.__cantidad}")

    def ingresar(self):
        if self.nueva_cantidad>=0:
            __cantidad+=nueva_cantidad

    def retirar(self):
        if self.nueva_cantidad<0:
            __cantidad+=nueva_cantidad