#! /usr/bin/python3

# Ejercicio 7_1. Escribir un programa que pregunte al usuario su nombre, 
# edad, dirección y teléfono y lo guarde en un diccionario. Después debe 
# mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en 
# <dirección> y su número de teléfono es <teléfono>

datUsu = {}

datUsu["name"] = input("Introduzca su nombre: ")
datUsu["edad"] = int(input("Introduzca su edad: "))
datUsu["dire"] = input("Introduzca su dirección: ")
datUsu["tel"] = input("Introduzca su teléfono: ")

print("%s tiene %s años, y vive en %s y su número de teléfono es %s." % (datUsu["name"],datUsu["edad"],datUsu["dire"],datUsu["tel"]))