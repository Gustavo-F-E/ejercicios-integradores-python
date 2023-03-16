#3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia). 

cadena="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

#Defino las variables vacías "lista_de_palabras" y "diccionario_de_palabras"

lista_de_palabras=[]
diccionario_de_palabras={}

#Despedazo el parrafo a partir de los espacios entre las palabras
lista_de_palabras= cadena.split(' ')

#Recorremos la lista de las palabras para que se forme el diccionario. La clave de este ejercicio es que a partir de las propiedades de los diccionarios (a partir de Python 3.7), los diccionarios son ordenados y además no tienen ítems repetidos
for i in range(0,len(lista_de_palabras),1):
    diccionario_de_palabras[lista_de_palabras[i]]=lista_de_palabras.count(lista_de_palabras[i])

#Imprimimos lo obtenido para verificar que esto funcionó correctamente
print(diccionario_de_palabras)
print(f"La longitud de la lista de las palabras es {len(lista_de_palabras)}, y la longitud del diccionario es {len(diccionario_de_palabras)}, con lo cuál había {len(lista_de_palabras)-len(diccionario_de_palabras)} palabras repetidas")