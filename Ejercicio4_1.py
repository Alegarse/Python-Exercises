#! /usr/bin/python3

# Ejercicio 4_1.  Pig Latin es un lenguaje creado en el que se toma la primera letra de una palabra 
# y se pone al final de la misma y se le agrega también el sonido vocálico “ei”. Por ejemplo, la 
# palabra perro sería "erropei". ¿Cuáles pasos debemos seguir?
# Pedir al usuario que ingrese una palabra en español.
# Verificar que el usuario introdujo una palabra válida.
# Convertir la palabra de español a Pig Latin.
# Mostrar el resultado de la traducción.

palabra = input("Introduzca una palabra en español: ")

while (palabra == ""):
    print("No has introducido ninguna palabra")
    palabra = input("Por favor, introduzca una palabra en español: ")

primeraletra = palabra[0]
longitud = len(palabra)
sinprimera = palabra[1:longitud]
palabra_pig = sinprimera + primeraletra + "ei"
print("La palabra introducida '%s' en idioma pig sería: %s" % (palabra,palabra_pig))




