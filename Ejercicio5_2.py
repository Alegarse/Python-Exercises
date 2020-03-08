#! /usr/bin/python3

# Ejercicio 5_2. Escribe un programa que tome como entrada el radio y 
# retorne el área de un círculo. El área de un círculo es igual a su 
# radio al cuadrado multiplicado por ´pi´. Usa math.pi para poder representar Pi.


import math

print("Programa que dado el radio devuelve el área del circulo.")
print("========================================================")

radio = int(input("Introduzca el radio deseado en mm: "))
area = radio * radio * math.pi
print("Dado un radio de %s mm, el área resultante del círculo es de: %.2f mm²" % (radio,area))

