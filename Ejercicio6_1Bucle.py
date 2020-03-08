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


altura=int(input("Introduzca la altura de la torre de Hanoi: "))
torre = range(1,altura+1)
pila1 = list(torre[::-1])
pila2 = []
pila3 = []
pila2.append(pila1.pop())
pila3.append(pila1.pop())

# Primerintento con comprobación entre pilas y posiciones. No sale
while (len(pila3) != altura):
        if (pila2[len(pila2)-1] > pila1[len(pila1)-1]):
           pila2.append(pila1.pop())
        if (pila3[len(pila3)-1] > pila1[len(pila1)-1]):
            pila3.append(pila1.pop())
        if (pila1[len(pila1)-1] > pila2[len(pila2)-1]):
            pila1.append(pila2.pop())
        if (pila3[len(pila3)-1] > pila2[len(pila2)-1]):
            pila3.append(pila2.pop())
        if (pila1[len(pila1)-1] > pila3[len(pila3)-1]):
            pila1.append(pila3.pop())
        if (pila2[len(pila2)-1] > pila3[len(pila3)-1]):
            pila2.append(pila3.pop())

# 2º Intento con lista de pilas y comprobar entre ellas
#pilas = ["pila1","pila2","pila3"]

#while (len(pila3) != altura):
#    for p in pilas:
#        if (p[len(p)-1] > 

print(pila1)
print(pila2)
print(pila3)