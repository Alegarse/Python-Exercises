#! /usr/bin/python3

# Ejercicio 1. Escriba un programa que pida una cantidad de segundos menor a 1 millón y que retorne cuántos días, horas, minutos y segundos son.

segundos=int(input("Cantidad de segundos menor a 1 millon: "))
if segundos>1000000:
	print("El numero debe ser menor a 1 millon")
	segundos=int(input("Cantidad de segundos menor a 1 millon: "))
else:		
	print ("Dias:%d - Horas:%d - Minutos:%d - Segundos:%d" % (segundos/86400,segundos%86400/3600,segundos%86400%3600/60,segundos%86400%3600%60))