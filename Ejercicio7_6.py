#! /usr/bin/python3

# Ejercicio 7_6. Escribir un programa que permita gestionar la base de datos de clientes de una empresa. 
# Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor 
# será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), 
# donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar 
# al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar 
# cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de 
# la opción elegida el programa tendrá que hacer lo siguiente:
# 
# Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
# Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
# Preguntar por el NIF del cliente y mostrar sus datos.
# Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
# Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
# Terminar el programa.


print("Gestión de base de datos empresarial")
print("====================================")
opt = 0
clientes = {}


while (opt !=6) :
    print("1. Introducir datos de cliente")
    print("2. Eliminar datos de cliente")
    print("3. Mostrar datos de cliente")
    print("4. Mostrar listado de clientes")
    print("5. Mostrar listado de clientes preferentes")
    print("6. Terminar")
    print("====================================")
    opt = int(input("Introduzca la opción elegida [1-6]: "))

    if opt == 6:
        print("\nGracias por usar este programa")
        print("Que tenga un buen día!")

    if opt == 1:
        dni = input("Introduzca el DNI del cliente: ")
        datos = {}
        datos["nombre"] = input("Introduzca el nombre del cliente: ")
        datos["direccion"] = input("Introduzca la dirección del cliente: ")
        datos["telefono"] = input("Introduzca el teléfono del cliente: ")
        datos["correo"] = input("Introduzca el correo del cliente: ")
        pref = input("Indique si es cliente preferente [S o N]: ")
        if (pref == "S"):
            datos["pref"] = True
        else:
            datos["pref"] = False 
        print(datos)
        clientes[dni]=datos
        print(clientes)
        datos = {}    
        print("\nVolviendo a menú principal....")
        print("\n")
    
    if opt == 2:
        borrado = input("Introduzca el DNI del cliente del cual desea eliminar sus datos: ")
        del clientes[borrado]
        print("Datos del DNI %s borrados correctamente." % borrado)
        print("\nVolviendo a menú principal....")
        print("\n")

    if opt == 3:
        iden = input("Introduzca el DNI del cliente para ver sus datos: ")
        print("\nDATOS DEL CLIENTE:")
        print("DNI: %s" % iden)
        for dni in clientes.keys():
            if dni == iden:
                for iden, valor in clientes.items():
                    for v in valor.keys():
                        print("%s: %s" % (v.capitalize(),valor[v]))
        print("\nVolviendo a menú principal....")
        print("\n")

    if opt == 4:
        print("\nMostrando listado de clientes: ")
        print("------------------------")
        for cliente in clientes:
            print("DNI: %s" % cliente)
            for dni, valor in clientes.items():
                    for v in valor.keys():
                        print("%s: %s" % (v.capitalize(),valor[v]))
            print("------------------------")
        print("\nVolviendo a menú principal....")
        print("\n")

    if opt == 5:
        print("\nMostrando listado de clientes preferentes: ")

        for cliente in clientes:
            if (datos.get("pref")):
                print("DNI: %s" % cliente)
                for dni, valor in clientes.items():
                    for v in valor.keys():
                        print("%s: %s" % (v.capitalize(),valor[v]))
                print("------------------------")
        print("\nVolviendo a menú principal....")
        print("\n")