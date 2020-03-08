#! /usr/bin/python3

# Ejercicio 9_1. Implementa el juego del AHORCADO, de modo que muestre por 
# pantalla los aciertos, los fallos, y el resultado parcial de la palabra. 
# Deberéis crear un archivo de palabras seleccionables, y el programa elegirá 
# una al azar en cada ejecución.

import random

print("Juego del ahorcado")
print("==================")

# Diccionario y selección aleatoria de la palabra al inicio del juego
palabras = {"1": "coche", "2": "autobus", "3": "moto","4": "comida","5": "programa","6": "oceano","7": "ordenador","8": "lenguaje","9": "externocleidomastoideo","10": "curso"}
longitud = len(palabras.keys())
numSeleccion = random.randint(1,longitud);
palabraSeleccionada = palabras[f"{numSeleccion}"]

print(palabraSeleccionada)
#print(len(palabraSeleccionada))

# Creamos un dicionario que contendrá la palabra que irá mostrando los aciertos
palabraODic = {}
for i in range(len(palabraSeleccionada)):
    palabraODic[i]= "-"

# Variables en el uso del juego
maxFallos = 7
fallos = 0
salir = False

while ((fallos < maxFallos) & (salir == False)):
    # Empieza el juego
    caracterE = input("Dime una letra: ")
    caracterElegido = caracterE.lower()
    # Si la palabra no contiene esa letra
    if (palabraSeleccionada.count(f"{caracterElegido}") < 1) :
        fallos +=1
        print(f"No existe la letra, llevas {fallos} fallo (máximo 7)")
    # Si la palabra contiene esa letra
    if (palabraSeleccionada.count(f"{caracterElegido}") >= 1) :
        print("Resultado = ", end="")
        for i in range(len(palabraSeleccionada)) :
            if palabraSeleccionada[i] == caracterElegido :
                palabraODic[i]=caracterElegido.upper()
        for j in range(len(palabraSeleccionada)) :
            print(palabraODic.get(j), end="")
        print("\n")
    # Si ya las ha acertado todas
        valores = palabraODic.values()
        caracterOculto = "-"
        if caracterOculto not in valores :
            print("¡ENHORABUENA!")
            salir = True

# Una vez cometemos todos los fallos permitidos
if fallos == maxFallos :
    print("\n¡LO SIENTO, HAS PERDIDO!")
