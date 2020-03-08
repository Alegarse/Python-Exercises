#! /usr/bin/python3

# Ejercicio 7_4. Escribir un programa que cree un diccionario simulando 
# una cesta de la compra. El programa debe preguntar el artículo y su 
# precio y añadir el par al diccionario, hasta que el usuario decida 
# terminar. Después se debe mostrar por pantalla la lista de la compra y 
# el coste total

cesta = {}

print("Cree su cesta de la compra.")
print("===========================")
print("Para salir escriba 'SALIR'")
salida = 0

while salida != 1:
    art = input("\nIntroduzca el artículo: ")
    if (art == "SALIR"):
        salida = 1
        break
    pre = float(input("Introduzca su precio: "))
    cesta[art]=pre

print("\nLista de la compra")
for arti in cesta.keys():
    print(arti, end="")
    print(" %s" % cesta.get(arti))
print("... ...")
suma = 0
for arti in cesta:
    suma += cesta[arti]
print("Total %s" % suma)