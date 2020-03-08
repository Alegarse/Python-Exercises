#! /usr/bin/python3

# Ejercicio 7_3. Escribir un programa que almacene el diccionario con los créditos 
# de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y 
# después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> 
# tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, 
# y <créditos> son sus créditos. Al final debe mostrar también el número total de 
# créditos del curso.

creditos = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

print("\nCurso actual matriculado")
print("========================")
for asig in creditos.keys():
    print(asig, end="")
    print(" tiene %s créditos." % creditos.get(asig))
sumC = 0
for asig in creditos:
    sumC += creditos[asig] 
print("\nEl total de créditos del curso es de %s créditos." % sumC)