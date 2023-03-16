#5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una  cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero  del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el  ejercicio tanto de manera iterativa como recursiva.

#Si defino dos variables e intento ejecutar lo siguiente:

var1=5
#var2="soy un string"

def convertir_a_numero_entero(x):
    print(int(x))

convertir_a_numero_entero(var1) #Por pantalla imprime el numero 5
#convertir_a_numero_entero(var2) #Por pantalla sale "ValueError: invalid literal for int() with base 10: 'soy un string' "

#Iterativa
def get_int_iterativa():
    iterativo=input("Ingrese un número entero:")
    while iterativo.isnumeric()==False or iterativo.isdigit()==False:
        iterativo=input("El número ingresado no era un número entero. Ingrese un número entero:")
    if iterativo.isdigit()==True: 
        print(f"El número ingresado es {iterativo}")

get_int_iterativa()

#Recursiva: evitar siempre que se pueda
def get_int_recursiva():
    try:
        recursivo=int(input("Ingrese un número entero: "))
    except:
        print(f"El número ingresado es no es un número entero")
        get_int_recursiva()
    else:
        print(f"El número ingresado es {recursivo}")

get_int_recursiva()