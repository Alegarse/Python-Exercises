#! /usr/bin/python3

# Ejercicio 10. Programación Orientada a Objetos

class Vehiculo() :

    cantidad = 0
    color = "Gris Amazonite"
    ancho = 2.098
    alto = 1.624
    largo = 4.447
    ruedas = 4
    gasolina = 3

    def __init__(self, nombre) :
        self.nombre = nombre
        Vehiculo.cantidad +=1
    
    def acelerar(self) :
        print("Acelera")
        Vehiculo.gasolina -= 1

    def frenar(self) :
        print("Frena")

    def arrancar(self) :
        if Vehiculo.gasolina >= 1 :
            print("Arranca")
            Vehiculo.gasolina -=1
        else :
            print("No arranca...")

    def conducir(self) :
        if Vehiculo.gasolina >=1 :
            Vehiculo.gasolina -= 1
            print("Quedan %d litros" % Vehiculo.gasolina)
        else :
            print("No se mueve...")

    def repostar(self) :
        Vehiculo.gasolina = 3
