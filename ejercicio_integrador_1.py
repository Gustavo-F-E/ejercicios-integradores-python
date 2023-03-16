#1. Escribir una función que calcule el máximo común divisor entre dos números. 
'''
En matemáticas, se denomina máximo común divisor o MCD al mayor número que divide exactamente a dos o más números a la vez. Como hablamos del mayor número solo tendremos en cuenta los divisores positivos.
También podemos decir que el máximo común divisor de dos números «A» y «B», es el número mayor que los divide a los dos, tanto al número A como al número B.
'''
#Lista de los valores involucrados en el Máximo común divisor MCD entre dos números a y b
MCD=[]

def maximo_comun_divisor():
    #El usuario define el primer número de la comparación
    a=int(input("Ingrese un número entero:"))
    print(f'El primer número ingresado es {a}')
    #El usuario define un segundo número de la comparación
    b=int(input("Ingrese otro número entero:"))
    print(f'El segundo número ingresado es {b}')
    #Hacemos una lista con los divisores del primer número
    divisores_de_a=[]
    for x in range(a,0,-1):
        if (a%x)==0:
            divisores_de_a.append(x)
    print(f"Los divisores del primer número son:{divisores_de_a}")
    #Hacemos una lista con los divisores del segundo número
    divisores_de_b=[]
    for x in range(b,0,-1):
        if (b%x)==0:
            divisores_de_b.append(x)
    print(f"Los divisores del segundo número son:{divisores_de_b}")
    #Hacemos una lista con los divisores en común
    divisores_en_comun=[]
    for i in range(0,len(divisores_de_a)):
        for j in range(0,len(divisores_de_b)):
            if divisores_de_a[i]==divisores_de_b[j]:
                divisores_en_comun.append(divisores_de_b[j])
    if len(divisores_en_comun)!=1:
        print(f"El máximo común divisor del primer número {a} y del segundo número {b} es {divisores_en_comun[0]}")
    else: print(f"El primer número ingresado {a} y el segundo número ingresado {b} no tienen divisores en común.")
    #Hacemos una lista con los valores involucrados
    MCD.append(a)
    MCD.append(b)
    MCD.append(divisores_en_comun[0])

maximo_comun_divisor()