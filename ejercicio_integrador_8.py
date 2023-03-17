#8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase  CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,  además del titular y la cantidad se debe guardar una bonificación que estará expresada en  tanto por ciento. Crear los siguientes métodos para la clase: 
#• Un constructor. 
#• Los setters y getters para el nuevo atributo. 
#• En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo  tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es  mayor de edad pero menor de 25 años y falso en caso contrario. 
#• Además, la retirada de dinero sólo se podrá hacer si el titular es válido. 
#• El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la  cuenta. 

from ejercicio_integrador_7 import Cuenta

class CuentaJoven(Cuenta):

    def __init__(self, nombre, edad, DNI, titular, cantidad, bonificacion="10%"):
        super().__init__(nombre, edad, DNI, titular, cantidad)
        self.__bonificacion = bonificacion

    def __str__(self):
        return super().__str__()+f"-{self.__bonificacion}"

    #Getters:
    @property
    def bonificacion(self):
        return self.__bonificacion

    #Setters:
    @bonificacion.setter
    def bonificacion(self, nueva_bonificacion):
        self.__bonificacion = nueva_bonificacion
    
    def es_titular_valido(self, edad):
        if edad<25 and edad>=18:
            print(True)
        else: print(False)
    
    def retirar(self, cantidad, es_titular_valido):
        if cantidad>0 and es_titular_valido==True:
            saldo_retirar=cantidad
            print(f"{self.__titular} retira ${saldo_retirar}")
            self.__cantidad-=cantidad
            print(f"El titular de la cuenta es  {self.__titular} y su saldo es ${self.__cantidad}")

    def mostrar3(self):
        print(f"Cuenta Joven: Bonificación del {self.__bonificacion}")

'''
cj1=CuentaJoven("Juan", 20,32456789,"Rafael",15000,"30%")
print(cj1)
cj1.mostrar1()
cj1.mostrar2()
print(cj1.bonificacion)
cj1.mostrar3()
'''
