#! /usr/bin/python3

# Ejercicio 5_1. Escribe un programa para jugar a adivinar un número (el ordenador 
# "piensa" el número y el usuario tiene que adivinarlo). El programa empieza pidiendo 
# entre qué números está el número a adivinar, se "inventa" un número al azar y 
# después el usuario va probando valores y el programa va diciendo si son demasiado 
#1 grandes o pequeños.


import random
from random import randrange

min = int(input("Valor mínimo: "))
max = int(input("Valor máximo: "))
print("A ver si adivinas un número entre el %s y el %s." % (min, max))
num = int(input("Escribe un número: "))
numero = random.randrange(min,max,1)
cont = 1

while (numero != num):
    if (num > numero):
        cont += 1
        num = int(input("¡Demasiado grande! Inténtalo de nuevo: "))
    if (num < numero):
        cont += 1
        num = int(input("¡Demasiado pequeño! Inténtalo de nuevo: "))

print("¡Acertaste! Te ha costado %s intentos" % cont)




-