#! /usr/bin/python3

# Ejercicio 3_1.  Escriba un programa que pida la anchura y altura de un rectángulo y lo dibuje con caracteres producto (*):

print("Vamos a dibujar un rectangulo dada su anchura y altura")
print("======================================================")
anch=int(input("Introduzca la anchura del rectangulo a pintar: "))
alt=int(input("Introduzca ahora su altura: "))
aux=anch-1
n=1
m=1
print("\nEste es el rectangulo: ")

#Parte superior
while n<=anch:
	print("*",end=" ")
	n+=1
alt-=1
print()

#Parte intermedia
while alt>1:
	print("*", end=" ")
	while aux>1:
		print(" ",end=" ")
		aux-=1
	print("*")
	aux=anch-1
	alt-=1

#Parte inferior
while m<=anch:
	print("*",end=" ")
	m+=1

