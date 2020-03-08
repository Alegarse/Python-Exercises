#! /usr/bin/python3

# Ejercicio 7_1. Escribir un programa que guarde en una variable el diccionario 
# {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y 
# muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divP = input("Escriba una divisa para saber su símbolo: ")

if (divP in divisas):
    print("El símbolo de la divisa %s es: %s" % (divP,divisas[divP]))
else:
    print("La divisa %s no existe en el diccionario." % divP)