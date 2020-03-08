#! /usr/bin/python3

# Ejercicio 4_3.  Escribir un programa que al introducir una palabra diga si es un palíndromo 
# (palabra, número o frase que se lee igual hacia adelante que hacia atrás). Ejemplo: ANA

print("\nPrograma que verifica si una palabra es un palíndromo")
print("=====================================================")

palabra = input("Introduzca una palabra para comprobar si es un palíndromo: ")

if (palabra.lower() == palabra[::-1].lower()):
    print("La palabra '%s' es un palíndromo." % palabra)
else:
    print("La palabra '%s' no es un palíndromo." % palabra)


