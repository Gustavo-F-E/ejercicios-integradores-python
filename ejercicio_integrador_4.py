#4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada  palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función  que reciba el diccionario generado con la función anterior y devuelva una tupla con la  palabra más repetida y su frecuencia. 

lista_de_palabras=[]
diccionario_de_palabras={}

def diccionario_de_frecuencias_de_palabras(cadena):
    #Utilizamos el programa que hicimos en el ejercicio anterior, pero esta vez lo utilizamos dentro de una función
    lista_de_palabras= cadena.split(' ')
    for i in range(0,len(lista_de_palabras),1):
        diccionario_de_palabras[lista_de_palabras[i]]=lista_de_palabras.count(lista_de_palabras[i])
    print(diccionario_de_palabras)
    print(f"La longitud de la lista de las palabras es {len(lista_de_palabras)}, y la longitud del diccionario es {len(diccionario_de_palabras)}, con lo cuál había {len(lista_de_palabras)-len(diccionario_de_palabras)} palabras repetidas")
    return diccionario_de_palabras

#Llamamos a una variable que nos ayude a ver si la función se ejecuta correctamente
lorem_ipsum="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."


#Llamamos a función
diccionario_de_frecuencias_de_palabras(lorem_ipsum)

#Ahora hacemos la funcion que haga una cupla. Para esto nos valemos de los métodos para hallar valores máximos en diccionarios.

def palabra_mas_repetida(diccionario):
    maximo_valor=max(diccionario.values())
    clave_de_maximo_valor=max(diccionario, key=diccionario.get)
    tupla_palabra_mas_repetida=(clave_de_maximo_valor,maximo_valor)
    print(tupla_palabra_mas_repetida)

palabra_mas_repetida(diccionario_de_palabras)