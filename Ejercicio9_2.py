#! /usr/bin/python3

# Ejercicio 9_2. Crear un fichero CSV con una estructura legible, en la que 
# se almacene información para una tienda de bicicletas. Los datos los irá 
# introduciendo el usuario hasta que inserte una secuencia para indicar que 
# ha terminado:

import csv

print("BICIS STORE S.A.")

fichero = open("bicisstore.csv","w")
contenido = csv.writer(fichero)
contenido.writerow(["MARCA", "MODELO", "PRECIO", "STOCK"])

noSalir = True

# Lectura de datos para incorporarlos al fichero
while (noSalir) :
    print("Introduzca los datos de la bicicleta ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    precio = input("Precio: ")
    stock = input("¿En stock?(s/n): ")
    contenido.writerow([marca,modelo,precio,stock])
    salida = input("¿Continuar introduciendo otra bicicleta?(s/n): ")
    if (salida == "n") :
        noSalir = False

fichero.close()