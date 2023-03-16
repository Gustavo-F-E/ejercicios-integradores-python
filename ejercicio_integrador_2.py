#2. Escribir una función que calcule el mínimo común múltiplo entre dos números
'''
En matemáticas, el mínimo común múltiplo (abreviado m.c.m) de dos o más números naturales es el menor múltiplo común de todos ellos.
Conociendo el máximo común divisor (MCD) de dos números, se puede calcular el mínimo común múltiplo de ellos (MCM), que será el producto de ambos dividido entre su máximo común divisor=>MCM=a.b/MCD.
'''
import ejercicio_integrador_1
ejercicio_integrador_1

def minimo_comun_multiplo():
    MCM=int(ejercicio_integrador_1.MCD[0]*ejercicio_integrador_1.MCD[1]/ejercicio_integrador_1.MCD[2])
    print(f"El mínimo común múltiplo entre {ejercicio_integrador_1.MCD[0]} y {ejercicio_integrador_1.MCD[1]} es {MCM}")

minimo_comun_multiplo()