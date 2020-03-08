#! /usr/bin/python3

# Ejercicio 3_2. Escriba un programa que pida la altura del dibujo y dibuje un árbol (triángulo sin base) con caracteres producto (*):

print("Vamos a dibujar un rectangulo dada su altura")
print("============================================")
alt=int(input("Introduzca la altura del triangulo a pintar: "))
n=1
hueco=1
print("\nEste es el triangulo: ")

#Parte superior
altAux=alt
while altAux>1:
	print(" ",end="")
	altAux-=1
print("*",end="")
altAux=alt
print()
alt-=1

#Parte intermedia
altAux=alt
while alt>1:
	while altAux>1:
		print(" ",end="")
		altAux-=1
	print("*",end="")
	altAux=alt
	while n<=hueco:
		print(" ",end="")
		n+=1
	print("*")
	hueco+=2
	n=1
	alt-=1
	altAux=alt

#Parte inferior
print("*",end="")
while n<=hueco:
		print(" ",end="")
		n+=1
print("*",end="")

