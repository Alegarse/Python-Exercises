#! /usr/bin/python3

# Ejercicio 8. Para este ejercicio hay que descargar el archivo de texto “ejemplo.txt” 
# y almacenarlo en la misma carpeta donde se guarda el programa. Este archivo contiene 
# una serie de emails donde hay que identificar las líneas que comienzan con el string 
# "X-DSPAM-Confidence:". Luego se identifica en que posición están los dos puntos (:) y 
# se extraen los caracteres que están a la derecha de los dos puntos, se transforma el 
# string leído a punto flotante, se suman los números leídos, se cuentan cuantas líneas 
# se seleccionaron y se calcula el promedio (suma de los números dividido por número 
# de líneas).

busqueda = 'X-DSPAM-Confidence:'
contador = 0

fichero =  open("Ejemplo.txt","r")
for row in fichero:
    if busqueda in row:
        posicion = row.find(':') + 1
        contador += float(row[posicion:])
print(contador)

fichero.close()