import json
from ModulReportes import *
from ModulBonificacion import *
from Clientes import *
    
print("Selccione una opcion")
print("1. Admin")
print("2. Usuario")
print("3. Servicios")

op= input(":")
    
match op:

    case "1":
        menuadmin()
    case "2":
        menuusuarios()
    case "3":
        pass
        



