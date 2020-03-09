#! /usr/bin/python3

# Ejercicio 10. Programación Orientada a Objetos

from claseVehiculo import Vehiculo

# Creo mi vehiculo

mi3008 = Vehiculo("Peugeot3008")

# Enumero las llamadas que se plantean en el Ejercicio

print(mi3008.gasolina)
mi3008.arrancar()
mi3008.conducir()
mi3008.conducir()
mi3008.conducir()
mi3008.conducir()
mi3008.arrancar()
print(mi3008.gasolina)