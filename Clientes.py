import json
from menus import *


usuarios=abrirJSON
def registrarse ():
    nombre= input("Ingrese su nombre completo")
    usuarios ["Nombre"].append(nombre)
    apellido= input ("Ingrese su apellido completo")
    usuarios ["Apellido"].append(apellido)
    dirrecion= input("Ingrese su dirrecion")
    usuarios ["Dirrecion"].append(dirrecion)
    numtel= input("Ingrese su numero de telefono")
    usuarios ["Celular"].append(numtel)
    guardarJSON
    
