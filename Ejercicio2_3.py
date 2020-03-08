#! /usr/bin/python3

# Ejercicio 3. Escriba un programa que pida tres números enteros y escriba la lista de números múltiplos del tercero 
# que hay entre los dos primeros (incluidos ellos mismos si son múltiplos del número indicado).

num1=int(input("Introduzca el primer numero: "))
num2=int(input("Introduzca el segundo numero: "))
num3=int(input("Introduzca el tercer numero: "))

posM = list(range(num1,num2+1))

print("\nLos multiplos de %d situados entre %d y %d son: " % (num3,num1,num2))
for n in posM:
	if n%num3 == 0:
		print(n, end=" ")