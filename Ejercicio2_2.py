#! /usr/bin/python3

# Ejercicio 2. Escriba un programa que pida dos números enteros m y n y escriba una lista de n números consecutivos a partir de m. 
# Utiliza la función range().

n=int(input("Introduzca un numero entero: "))
m=int(input("Introduzca otro numero entero: "))
num=m+n
sucesion=list(range(m,num))
print(sucesion)