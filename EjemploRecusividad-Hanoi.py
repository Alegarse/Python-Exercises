#! /usr/bin/python3

# Ejercicio 6_1. Las torres de Hanoi. El rompecabezas de las Torres 
# de Hanoi fue inventado por el matemático francés Edouard Lucas en 1883. Se 
# inspiró en una leyenda acerca de un templo hindú donde el rompecabezas fue 
# presentado a los jóvenes sacerdotes. Al principio de los tiempos, a los 
# sacerdotes se les dieron tres postes y una pila de 64 discos de oro, cada 
# disco un poco más pequeño que el de debajo. Su misión era transferir los 
# 64 discos de uno de los tres postes a otro, con dos limitaciones importantes. 
# Sólo podían mover un disco a la vez, y nunca podían colocar un disco más grande 
# encima de uno más pequeño. Los sacerdotes trabajaban muy eficientemente, día y 
# noche, moviendo un disco cada segundo. Cuando terminaran su trabajo, dice la 
# leyenda, el templo se desmenuzaría en polvo y el mundo se desvanecería.
# 
# Realiza un programa utilizando listas que nos permita resolver el problema.

print("Resolucion de la torre de Hanoi")
print("===============================")
altura = int(input("\nIntroduzca la altura de la torre: "))

def cambiaT(alt,origen, dest, intermedio):
    if alt >= 1:
        cambiaT(alt-1,origen,intermedio,dest)
        cambiaD(origen,dest)
        cambiaT(alt-1,intermedio,dest,origen)

def cambiaD(desde,hacia):
    print("mover disco de",desde,"a",hacia)

cambiaT(altura,"Torre 1","Torre 2","Torre 3")