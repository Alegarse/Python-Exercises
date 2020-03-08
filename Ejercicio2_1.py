#! /usr/bin/python3

# Ejercicio 1. Escribir un algoritmo que simule el funcionamiento de una calculadora. 
# El dato es una serie de tres caracteres: una cifra, un símbolo de operación y otra cifra. El resultado es el valor de la expresión dada.

cifra1=int(input("Introduzca la primera cifra: "))
oper=input("Introduzca la operacion [+, -, *, /]: ")
cifra2=int(input("Introduzca la segunda cifra: "))

if oper == "+":
	print("Resultado: %.2f " % (cifra1+cifra2))
elif oper == "-":
	print("Resultado: %.2f " % (cifra1-cifra2))
elif oper == "*":
	print("Resultado: %.2f " % (cifra1*cifra2))
elif oper == "/":
	print("Resultado: %.2f " % (cifra1/cifra2))