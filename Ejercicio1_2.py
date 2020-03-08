#! /usr/bin/python3

# Ejercicio 2. Escribir un algoritmo que imprima el mínimo, el máximo y la media de tres números.

lista=[0,0,0]
lista[0]=int(input("Introduce el primer numero: "))
lista[1]=int(input("Introduce el segundo numero: "))
lista[2]=int(input("Introduce el tercer numero: "))
print("El minimo es el numero " + str(min(lista)))
print("El maximo es el numero " + str(max(lista)))
print("La media de los numeros es %.2f" % ((lista[0]+lista[1]+lista[2])/3))