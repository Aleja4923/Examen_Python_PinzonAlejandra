import json
from ModulReportes import *
from ModulBonificacion import * 
from Clientes import *


def abrirJSON():
    dicFinal={}
    with open('./bbdd_Fut.json','r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./bbdd_Fut.json",'w') as outFile:
        json.dump(dic,outFile)

usuarios = abrirJSON

def menuadmin ():
    print("Selccione una opcion")
    print("1. Agregar usuarios")
    print("2. Editar usuarios")
    print("3. Ver usuarios")
    print("4. Eliminar usuarios")
    print("5. Modulo reportes")
    opt=input(" ")

    match opt:
        case "1":
            registrarusers ()
        case "2":
            verusers()
        case "3":
            pass
        case "4":
            pass
            


def menuusuarios ():
    
        print("Selccione una opcion")
        print("1. Registrarse")
        print("2. Ver ofertas personalizadas")
        print("3. Quejas")
        print("4. Bonificaciones especiales")
        opc=input(" ")

        match opc:
            case "1":
                registrarusers ()
            case "2":
                pass
            case "3":
                pass
            case "4":
                bonificaciones()
