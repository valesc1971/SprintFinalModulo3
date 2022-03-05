from Modulo_3_Sprint_Bodega import *

compra_despacho=[]
bodega_A=[]
bodega_B=[]

def restar_stock_despacho():
    bodega_dicc=generacion_dicc()   #importa el listado de productos desde Modulo_3_Sprint_Bodega
    print('\nListado de productos\n')
    print('\nPRODUCTO\t\tDESCRIPCION\t\t\tSTOCK\n')
    for prod,val in bodega_dicc.items():        #imprime listado de productos
        print(prod,'\t\t',val[0],'\t\t',val[1])    
    preguntar=True
    while preguntar:
        producto = input("\nSeleccione el producto que quiere despachar: ")
        if producto in bodega_dicc.keys():      #recorre diccionario de productos
                unidades=int(input('\nIngrese unidades a enviar '))
                for prod,valor in bodega_dicc.items():
                        if producto in prod:
                                preguntar=False
                                if unidades<valor[1]:   #revisa q haya unidades disponibles en stock para enviar
                                    valor[1]=valor[1]-unidades
                                else:
                                    print('\nEl stock no es suficiente')
                                    preguntar=True
        else:
            print('\nEl producto ingresado no existe ')
            preguntar=True
    compra_despacho.append([producto,unidades]) #en caso de que el producto exista y haya unidades suficentes en inventario, almacena la venta en una lista
    #print(compra_despacho)
    return unidades

def tipo_envio():       #define si envio es rapido o largo en base a la distancia de envio solicitad apor consola
    unidades_despachar=restar_stock_despacho()      #importa desde la funcion restar_stock_despacho las unidades a despachar (ya validad con stock)
    resp_envio=True
    while resp_envio:
        envio=input('\nIngrese distancia de despacho: ')
        if envio.isdigit():
            if int(envio)>1000: #revisa si sitancia es > 1000 para enviar a bodega B
                bodega_B.append(unidades_despachar)  #agrega las unidades a la Bodega B
                #print(bodega_B)
                sum_bod_B=int(sum(bodega_B))    #suma las unidades que se encuentran en bodega B para ccomprobar q no sobrepase las 500 unidades
                if sum_bod_B<500:
                    print('\nEl envio de su compra es considerado "largo"')
                    print('\nSu compra se ha asignado a Bodega B')
                    resp_envio=False
                else:
                    print('\nNo se puede almacenar mas unidades en la Bodega B')
            elif int(envio)<=1000:   #revisa si sitancia es <= 1000 para enviar a bodega A
                bodega_A.append(unidades_despachar)  #agrega las unidades a la Bodega B
                sum_bod_A=int(sum(bodega_A))  #suma las unidades que se encuentran en bodega B para ccomprobar q no sobrepase las 500 unidades
                if sum_bod_A<500:
                    print('\nEl envio de su compra es considerado "rapido"')
                    print('\nSu compra se ha asignado a Bodega A')
                    resp_envio=False
                else:
                    print('\nNo se puede almacenar mas unidades en la Bodega A')                
            else:
                print('\nValor ingresado no valido')
            break
        else:
            print('\nValor ingresado no valido')
            resp_envio=True
    #print(bodega_A)
    #print(bodega_B)
    print('\nSi desea ingresar otro despacho, ingrese a la opcion 1 del Menu Despachos\n')

def funcion_despacho():     #ejecucion de la funcion de despacho
    #bodega_dicc={'cucharas': ['es una cuchara', 425], 'tazas': ['        es una taza    ', 427], 'cuchillo': ['es un cuchillos', 431], 'tenedor': ['es un tenedor  ', 461]}
    
    solicitud_ingreso = True
    while solicitud_ingreso:
                    print('\n','-'*40, 'MENU DESPACHO', '-'*40,'\n')      # despliega menu de bodega
                    info_clientes_menu = input("1 Ingresar un despacho\n2 Salir\n")
                    if info_clientes_menu == "1":
                        tipo_envio()       #agrega nuevos clientes
                    elif info_clientes_menu == "2":
                        solicitud_ingreso = False       #sale del menu
                    else:
                        print("Opción no válida")






