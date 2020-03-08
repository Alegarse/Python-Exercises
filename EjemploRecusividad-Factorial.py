#! /usr/bin/python3

# Ejercicio Recursividad. Resulver el factorial de un número.

print("Resolucion del factorial de un número.")
print("======================================")

n = int(input("Introduzca el número al que calcular el factorial: "))
resultado = 0

def factN(n):
   if (n == 0 or n == 1):
      return 1
   else:
      return n * factN(n - 1)

resultado = factN(n)
print(resultado)