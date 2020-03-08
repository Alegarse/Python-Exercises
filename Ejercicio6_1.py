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

num=int(input("Introduzca la altura de la torre de Hanoi (2 o 3): "))

if (num == 2):
    pila1=[2,1]
    pila2=[0,0]
    pila3=[0,0] 
    print("Estado inicial de las torres: ",end=" ")
    print("Torre 1: %s , Torre 2: %s ,Torre 3: %s" % (pila1,pila2,pila3))
    pila2[0]=pila1[1]
    pila3[0]=pila1[0]
    pila3[1]=pila2[0]
    pila1 = [0,0]
    pila2 = [0,0]
    print("Estado final de las torres:   ",end=" ")
    print("Torre 1: %s , Torre 2: %s , Torre 3: %s" % (pila1,pila2,pila3))

if (num == 3):
    pila1 = [3,2,1]
    pila2 = [0,0,0]
    pila3 = [0,0,0]
    print("Estado inicial de las torres: ",end=" ")
    print("Torre 1: %s , Torre 2: %s , Torre 3: %s" % (pila1,pila2,pila3))
    pila3[0]=pila1[2]
    pila2[0]=pila1[1]
    pila2[1]=pila3[0]
    pila3[0]=pila1[0]
    pila1[0]=pila2[1]
    pila3[1]=pila2[0]
    pila3[2]=pila1[0]
    pila1 = [0,0,0]
    pila2 = [0,0,0]
    print("Estado final de las torres:   ",end=" ")
    print("Torre 1: %s , Torre 2: %s , Torre 3: %s" % (pila1,pila2,pila3))



