import random
bodega_dicc={'cucharas':['es una cuchara'],'tazas':['        es una taza    '], 'cuchillo': ['es un cuchillos'],'tenedor': ['es un tenedor  ']}
#llenado con random
def generacion_dicc():  #generacion de unidades de stock en forma aleatorioa entre 300 y 500
    for k in bodega_dicc.keys():
            bodega_dicc[k].append(random.randint(300,500))
    bodega=bodega_dicc
    return bodega
#sumar unidades
def sumar_stock():      #agrega unidades al stock inicial
    print('\nListado de productos\n')       #imprime listado inicial de productos
    print('\nPRODUCTO\t\tDESCRIPCION\t\t\tSTOCK\n')
    for prod,val in bodega_dicc.items():
        print(prod,'\t\t',val[0],'\t\t',val[1])
    preguntar=True
    while preguntar:
        producto = input("\nSeleccione el producto que quiere actualizar: ")
        if producto in bodega_dicc.keys():              #validacion para compraobar que producto se encuentre en el listado de productos
                unidades=int(input('\nIngrese las unidades a agregar: '))
                for prod,valor in bodega_dicc.items():
                    if producto in prod:
                        preguntar=False
                        valor[1]=valor[1]+unidades      #agrega las unidades ingresadas
        else:
            print('\nEl producto ingresado no existe ')
            preguntar=True
    print('\nListado de productos actualizado\n')
    print('\nPRODUCTO\t\tDESCRIPCION\t\t\tSTOCK\n')     #imprime listado de productos actualizados
    for prod,val in bodega_dicc.items():
        print(prod,'\t\t',val[0],'\t\t',val[1])
    print('\nSi desea agregar unidades a otro producto, seleccione la opcion 1 del Menu Bodega\n')
#resta unidades
def restar_stock():     #resta unidades al stock inicial
    print('\nListado de productos\n')       #imprime stock prouctos inicial
    print('\nPRODUCTO\t\tDESCRIPCION\t\t\tSTOCK\n')
    for prod,val in bodega_dicc.items():
        print(prod,'\t\t',val[0],'\t\t',val[1])    
    preguntar=True
    while preguntar:
        producto = input("\nSeleccione el producto que quiere actualizar: ")
        if producto in bodega_dicc.keys():      #valida que producto se encuentre entre los productos del listado
                unidades=int(input('\nIngrese unidades a restar '))
                for prod,valor in bodega_dicc.items():
                        if producto in prod:
                                preguntar=False
                                if unidades<valor[1]:       #valida que se encuntren unidades disponibles en stock
                                    valor[1]=valor[1]-unidades      #resta las unidades deseadas
                                else:
                                    print('\nEl stock no es suficiente')
                                    preguntar=True
        else:
            print('\nEl producto ingresado no existe ')
            preguntar=True
    print('\nListado de productos actualizado\n')       #imprime listado de productos actualizado
    print('\nPRODUCTO\t\tDESCRIPCION\t\t\tSTOCK\n')
    for prod,val in bodega_dicc.items():
        print(prod,'\t\t',val[0],'\t\t',val[1])
    print('\nSi desea restar unidades a otro producto, seleccione la opcion 2 del Menu Bodega\n')
#ingresa producto nuevo
def actualizar_stock():         #ingresa producto nuevo y lo almacena en diccionario stock{}
    producto = input("\nIngrese un nuevo producto: ")
    while producto in bodega_dicc.keys(): #validacion para ingresar un producto que no este en stock{}
        print('\nProducto ingresado ya se encuentra en el listado de producto\n')
        producto = input("\nIngrese un nuevo producto: ")    #ingresa producto nuevo
    if producto not in bodega_dicc.keys():
        descripcion=input('\nIngrese la descripcion del producto: ')
        valor = int(input("\nIngrese la cantidad del nuevo producto: ")) #ingreso del stock de producto nuevo
        bodega_dicc[producto]=[descripcion,valor]   #almcena el producto nuevo y su stock en {stock}
        print('\nEl producto ingresado es: ', producto,' su descripcion es ', descripcion,' y su stock es ', valor)
    print('\nListado de productos actualizado\n')
    print('\nPRODUCTO\t\tDESCRIPCION\t\t\tSTOCK\n')     #imprime listado de productos actualizado
    for prod,val in bodega_dicc.items():
        print(prod,'\t\t',val[0],'\t\t',val[1])
    print('\nSi desea ingresar otro producto, seleccione la opcion 4 del Menu Bodega\n')
#elimina producto
def eliminar_producto():
    print('\nListado de productos\n')
    print('\nPRODUCTO\t\tDESCRIPCION\t\t\tSTOCK\n')     #imprime listado inicial de productos
    for prod,val in bodega_dicc.items():
        print(prod,'\t\t',val[0],'\t\t',val[1])        
    producto=input('ingrese producto a remover ')
    while producto not in bodega_dicc.keys(): #validacion para comproabar q producto  este en stock{}
        print('\nProducto ingresado no se encuentra en el listado de producto\n')
        producto=input('Ingrese producto a remover')
    if producto in bodega_dicc.keys():
        bodega_dicc.pop(producto)       #elimina producto
        print('El producto eliminado es: ', producto)
    print('\nListado de productos actualizado\n')       #imprime lista de productos actualizada
    print('\nPRODUCTO\t\tDESCRIPCION\t\t\tSTOCK\n')
    for prod,val in bodega_dicc.items():
        print(prod,'\t\t',val[0],'\t\t',val[1])
    print('\nSi desea eliminar otro producto, seleccione la opcion 3 del Menu Bodega\n')
#despliega productos disponibles
def mostrar_prod_disponibles():     #imprime productos en listado en forma tabular
    print('\nPRODUCTO\t\tDESCRIPCION\t\t\tSTOCK\n')
    for prod,val in bodega_dicc.items():
        print(prod,'\t\t',val[0],'\t\t',val[1])
    print()
#verifica productos con stock < 400 u
def verificar_stock_400():      #verifica stock de productos > 0 < q 400 u
    preguntar=True
    while preguntar:
        producto = input("\nSeleccione el producto que quiere verificar: ")
        if producto in bodega_dicc.keys():      #recorres diccionario para buscar el producto y verificar que se encuentre en el listado
                for prod,valor in bodega_dicc.items():
                        if producto in prod:
                                preguntar=False
                                if valor[1]<400:    #revisa que el stock para ese producto sea menor q 400 u
                                    print('\n*****ATENCION - producto con stock menor q 400 unidades*****\n')       #imprime alarma
                                else:
                                    print("\nEl producto tiene un inventario mayor o igual a 400 unidades\n")
        else:
            print('\nel producto ingresado no existe \n')
            preguntar=True
    print('\nSi desea verificar si otro producto tiene un stock menor a 400 unidades, seleccione la opcion 6 del Menu Bodega\n')            
            
#### menu ###

def funcion_bodega():       #funcion de ejecucion para el menu de bbodega
    generacion_dicc()
    solicitud_ingreso = True
    while solicitud_ingreso:
                    print('\n','-'*40, 'MENU BODEGA', '-'*40,'\n')      # despliega menu de bodega
                    info_bodega_menu = input("1 Agregar unidades a 1 producto \n2 Restar unidades a 1 producto \n3 Eliminar 1 producto\n4 Agregar 1 producto nuevo\n5 Mostrar listado productos y stock disponible\n6 Revisar productos con menos de 400 unidades en stock\n7 Salir\n")
                    if info_bodega_menu == "1":
                        sumar_stock()       #suma unidades al stock
                    elif info_bodega_menu == "2":
                        restar_stock()                 #resta unidades al stock
                    elif info_bodega_menu == "3":
                        eliminar_producto()                        #elimina producto  
                    elif info_bodega_menu == "4":
                        actualizar_stock()                #ingresar producto nuevo
                    elif info_bodega_menu == "5":
                        mostrar_prod_disponibles()                 #muestra productos 
                    elif info_bodega_menu == "6":
                        verificar_stock_400()                        #productos con menos de 400 u 
                    elif info_bodega_menu == "7":
                        solicitud_ingreso = False       #sale del menu
                        respuesta_menu=True
                    else:
                        print("Opción no válida")




