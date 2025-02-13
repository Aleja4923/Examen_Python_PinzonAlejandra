import json
from menus import *


usuarios = abrirJSON
def registrarusers ():
    nombre= input("Ingrese el nombre completo")
    usuarios ["Nombre"].append(nombre)
    apellido= input ("Ingrese el apellido completo")
    usuarios ["Apellido"].append(apellido)
    dirrecion= input("Ingrese la dirrecion")
    usuarios ["Dirrecion"].append(dirrecion)
    numtel= input("Ingrese  numero de telefono")
    usuarios ["Celular"].append(numtel)
    guardarJSON

def verusers():
    for i in range (len(usuarios["Usuarios"])):
        print ("Usuarios #",i+1,usuarios["Usuarios"])
