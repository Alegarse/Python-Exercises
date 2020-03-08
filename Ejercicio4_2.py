#! /usr/bin/python3

# Ejercicio 4_2.  Escribe un programa que pida dos cadenas de caracteres e indique 
# si la segunda cadena es una subcadena de la primera. Por ejemplo, lago es una 
# subcadena de murciélago.

print("\nPrograma que verifica si de dos cadenas introducidas ,la segunda es subcadena de la primera")
print("===========================================================================================")

cadena1 = input("Introduzca una cadena de caracteres: ")
while (cadena1 == ""):
    print("No has introducido ninguna cadena")
    cadena1 = input("Por favor, introduzca la primera cadena de caracteres: ")
cadena2 = input("Introduzca otra cadena de caracteres: ")
while (cadena2 == ""):
    print("No has introducido ninguna cadena")
    cadena2 = input("Por favor, introduzca la segunda cadena de caracteres: ")

if (cadena2 in cadena1):
    print("La cadena de caracteres '%s' está contenida en la cadena '%s'" % (cadena2, cadena1))
else:
    print("La cadena de caracteres'%s' no está contenida en la cadena '%s'" % (cadena2, cadena1))



