#! /usr/bin/python3

# Ejercicio 7_5. Escribir un programa que cree un diccionario de 
# traducción español-inglés. El usuario introducirá las palabras 
# en español e inglés separadas por dos puntos, y cada par 
# <palabra>:<traducción> separados por comas. El programa debe 
# crear un diccionario con las palabras y sus traducciones. Después 
# pedirá una frase en español y utilizará el diccionario para 
# traducirla palabra a palabra. Si una palabra no está en el 
# diccionario debe dejarla sin traducir.

dic = {}
finD = 0

print("Diccionario traducción Español-Inglés")
print("=====================================")
print("\n## Vamos a construir el traductor ##")
print("  (( Para finalizar escriba FIN ))")

while finD != 1:
    esp = input("Introduzca la palabra en español: ")
    if (esp == "FIN"):
        findD = 1
        print("Construcción de diccionario finalizada")
        break
    ing = input("Introduzca su traducción al inglés: ")
    dic[esp]=ing

print("\nVamos ahora a probar el traductor")
fraseI = input("Introduzca una frase: ")
frase = fraseI.split()
i = 0

for word in frase:
    for p in dic.keys():
        if p == word:
            frase[i] = dic.get(p)
    i += 1

print("La frase traducida al inglés es:")
for i in frase:
    print(i, end=" ")