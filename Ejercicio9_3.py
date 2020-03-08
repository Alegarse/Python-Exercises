#! /usr/bin/python3

# Ejercicio 9_2. Crear un fichero CSV con una estructura legible, en la que 
# se almacene información para una tienda de bicicletas. Los datos los irá 
# introduciendo el usuario hasta que inserte una secuencia para indicar que 
# ha terminado:

import csv

print("BICIS STORE S.A.\n")

fichero = open("bicisstore.csv","r")
contenido = csv.reader(fichero)

listadoBicis = list(contenido)
print(listadoBicis)

for row in listadoBicis: 
    for col in row :
        print(col, end="\t")
    print("\n")




fichero.close()