#! /usr/bin/python3

# Ejercicio Recursividad. Resulver el factorial de un número.

print("Mostrar elementos de una lista de forma recursiva a la inversa")
print("==============================================================")

long = int(input("Introduzca el tamaño de la lista: "))

lista = [1,4,7,3,8,4,9,7,5,2,0,3]
n = len(lista)

def muestraL(n) :
    if (n == 1) :
        print(lista[n-1], end=" ")
    else:
        print(lista[n-1], end=" ")
        muestraL(n-1)

muestraL(n)