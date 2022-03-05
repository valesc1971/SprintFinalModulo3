from Modulo_3_Sprint_Bodega import *
from Modulo_3_Sprint_Clientes import *
from Modulo_3_Sprint_Despacho import *


solicitud_menu_principal = True
while solicitud_menu_principal:
    print('\n','-'*40, 'MENU PRINCIPAL', '-'*40,'\n')      # despliega menu de bodega
    info_menu_principal = input("1 Ingresar a BODEGA\n2 Ingresar a CLIENTES\n3 Ingresar a DESPACHOS\n4 Salir\n")
    if info_menu_principal == "1":
        funcion_bodega()       #menu BODEGA
    elif info_menu_principal == "2":
        funcion_cliente()      #menu CLIENTES
    elif info_menu_principal == "3":
        funcion_despacho()      #menu DESPACHO
    elif info_menu_principal == "4":
        solicitud_menu_principal = False       #sale del menu
    else:
        print("Opción no válida")

