import random
import string

usuario_lista=[]    #lista donde almacena el dato de 1 usuario
datos_user=[]       #lista de listas - almacenan las listas de los usuarios individuales
usuario_check=[]    #lista para almacenar usuarios y verificar que sea un usuario nuevo
usuario_check_intentos=[] #lista q almacena cada intento fallido (usuario en lista anterior)
#usuario_nombre_appellido_edad=[['vale', 'valeriaa', 'sanchez', 'Vale1', '8'], ['oli', 'olivia', 'castro', 'Oli1', '9'], ['ele', 'elena', 'castro', 'Ele1', '3']]
usuario_nombre_appellido_edad=[]

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
letters_low=string.ascii_lowercase

def listado_inicial(): #generacion de listado de clientes usando funciones random
    for i in range (0,5):
        user_random=''.join(random.choice(letters_low) for i in range(4))
        nombre_random=''.join(random.choice(letters_low) for i in range(6))
        apellido_random=''.join(random.choice(letters_low) for i in range(8))
        password_random = ''.join(random.choice(characters) for i in range(8))
        edad=_random=random.randint(15,65)
        usuario_nombre_appellido_edad.append([user_random, nombre_random,apellido_random,password_random,edad])

    #print(usuario_nombre_appellido_edad)
    return usuario_nombre_appellido_edad # retorna listado inicial de clientes para trabajar

def valida_usuarios(): #valida 'usuario" para verificar que no se haya ingresado antes
        usuario=input('\nIngrese usuario de cliente nuevo: ')  ####nombre usuario por consola
        for i in range (0,len(usuario_nombre_appellido_edad)):
            while usuario in usuario_nombre_appellido_edad[i][0]:
                usuario=input('usuario ya registrado. ingrese un nuevo usuario: ')
        if usuario not in usuario_nombre_appellido_edad[i][0]:
            return usuario
        
def valida_nombre():        #valida nombre de tal forma de que se ingresen solo letras
    nombre=(input('\ningrese nombre: ')).lower()  ####nombre por consola)
    while any(char.isdigit() for char in nombre):
        nombre=(input('\ningrese nombre: ')).lower() 
    return nombre

def valida_apellido():   #valida apellido de tal forma de que se ingresen solo letras
    apellido=(input('\ningrese apellido: ')).lower()  ####nombre por consola)
    while any(char.isdigit() for char in apellido):
        apellido=(input('\ningrese apellido: ')).lower() 
    return apellido 

def valida_password():      #valida password para q tenga al menos 8 caracteres, 1 mayuscula, 1 minuscula y 1 numero.
    while True:         #while loop para revisar password valida
        clave=input('\ningrese password: ')  ###password por consola
        if len(clave)<8:
            print('Su clave debe tener al menos 8 caracteres')
        elif not any(char.islower() for char in clave):
            print('Su clave debe tener al menos 1 letra minuscula')
        elif not any(char.isupper() for char in clave):
            print('Su password debe tener al menos 1 letra mayuscula')
        elif not any(char.isdigit() for char in clave ):
            print('Su password debe tener al menos numero')
        else:
            print('password OK')
            break
    return clave

def valida_numero_edad():       #valida edad para q sea un numero entero
    edad=True
    while edad:
        edad=input('\nIngrese edad: ')    #edad por consola
        if edad.isdigit():
            break
    return edad    

def ejecucion_agregar_usuarios():       #agrega un usuario nuevo.
    print('\nListado de clientes\n')    
    print('\nUSUARIO\t\tNOMBRE\t\t\tAPELLIDO\t\tPASSWORD\t\tEDAD\n')
    for i in range(0,len(usuario_nombre_appellido_edad)):
        print(usuario_nombre_appellido_edad[i][0],'\t\t',usuario_nombre_appellido_edad[i][1],'\t\t',usuario_nombre_appellido_edad[i][2],'\t\t',usuario_nombre_appellido_edad[i][3],'\t\t',usuario_nombre_appellido_edad[i][4] )    
    usuario=valida_usuarios()       #asigna los returns de las funciones anteriores para generar la listaa (usuario, nombre, apellido, password y edad)
    nombre=valida_nombre()
    apellido=valida_apellido()
    password=valida_password()
    edad=valida_numero_edad()
    usuario_nombre_appellido_edad.append([usuario,nombre,apellido,password,edad]) #genera la lista individual
    #print(usuario_nombre_appellido_edad)
    indice_usuario_nuevo=(len(usuario_nombre_appellido_edad)-1)
    print('\nEl cliente nuevo creado es:\n')
    for i in range (0,4):
        print(usuario_nombre_appellido_edad[indice_usuario_nuevo][i] )  #imprime el usuario nuevo
    print('\nListado de clientes actualizado\n')
    print('\nUSUARIO\t\tNOMBRE\t\t\tAPELLIDO\t\tPASSWORD\t\tEDAD\n') #imprime listado actualizado
    for i in range(0,len(usuario_nombre_appellido_edad)):
        print(usuario_nombre_appellido_edad[i][0],'\t\t',usuario_nombre_appellido_edad[i][1],'\t\t',usuario_nombre_appellido_edad[i][2],'\t\t',usuario_nombre_appellido_edad[i][3],'\t\t',usuario_nombre_appellido_edad[i][4] )    
    print('\nPara ingresar un cliente nuevo ingrese 1 en el Menu Clientes')
    return usuario_nombre_appellido_edad

#### muestra lista clientes ####
def lista_info_cliente():       #imprime lista de clientes
    print('\nListado de clientes\n')
    print('\nUSUARIO\t\tNOMBRE\t\t\tAPELLIDO\t\tPASSWORD\t\tEDAD\n')
    for i in range(0,len(usuario_nombre_appellido_edad)):
        print(usuario_nombre_appellido_edad[i][0],'\t\t',usuario_nombre_appellido_edad[i][1],'\t\t',usuario_nombre_appellido_edad[i][2],'\t\t',usuario_nombre_appellido_edad[i][3],'\t\t',usuario_nombre_appellido_edad[i][4] )
    print('\nSi desea revisar nuevamente el listado de clientes, ingrese a la opcion 3 del Menu Clientes\n')

#lista_info_cliente()
def elimina_usuario():      #elimina usuario
    print('\nListado de clientes')      #imprime listado inicial de clientes
    print('\nUSUARIO\t\tNOMBRE\t\tAPELLIDO\t\tPASSWORD\t\tEDAD\n')
    for i in range(0,len(usuario_nombre_appellido_edad)):
        print(usuario_nombre_appellido_edad[i][0],'\t\t', usuario_nombre_appellido_edad[i][1],'\t\t',usuario_nombre_appellido_edad[i][2],'\t\t',usuario_nombre_appellido_edad[i][3],'\t\t',usuario_nombre_appellido_edad[i][4] )
    usuario_eliminar=input('Ingrese cliente a eliminar ')   #ingresa usuario a eliminar
    for i in range (0,len(usuario_nombre_appellido_edad)):  #recorre lista par encontrar usuario a eliminar
        if usuario_eliminar in usuario_nombre_appellido_edad[i][0]: 
            (usuario_nombre_appellido_edad[i])
            indice=usuario_nombre_appellido_edad.index(usuario_nombre_appellido_edad[i])    #busca el indice en que el usuario a eliminar se encuentra en la lista que almacenaa los usuarios
            #print(indice)
    usuario_eliminado=usuario_nombre_appellido_edad.pop(indice)     #para el usuario a eliminar, elmina la lista individual que contiene la info de ese usuario
    print('\nEl cliente eliminado es:\n')
    for i in range (0,4):
        print(usuario_eliminado)        #print de usuario eliminado
    #print(usuario_nombre_appellido_edad)
    print('\nListado de clientes actualizado\n')
    print('\nUSUARIO\t\tNOMBRE\t\t\tAPELLIDO\t\tPASSWORD\t\tEDAD\n')    #impresion de la lista ctualizada de usuarios
    for i in range(0,len(usuario_nombre_appellido_edad)):
        print(usuario_nombre_appellido_edad[i][0],'\t\t',usuario_nombre_appellido_edad[i][1],'\t\t',usuario_nombre_appellido_edad[i][2],'\t\t',usuario_nombre_appellido_edad[i][3],'\t\t',usuario_nombre_appellido_edad[i][4] )    
    
    print('\nSi desea eliminar otro cliente, ingrese a la opcion 2 del Menu Clientes\n')


#### menu ###
def funcion_cliente():      #funcion principal que va llamando a las otras funciones para ejecutar el programa en base a un menu
    listado_inicial()
    solicitud_ingreso = True
    while solicitud_ingreso:
                    print('\n','-'*40, 'MENU CLIENTES', '-'*40,'\n')      # despliega menu de bodega
                    info_clientes_menu = input("1 Agregar nuevos clientes\n2 Eliminar clientes por ID \n3 Mostrar informacion por cliente \n4 Salir\n")
                    if info_clientes_menu == "1":
                        ejecucion_agregar_usuarios()       #agrega nuevos clientes
                    elif info_clientes_menu == "2":
                        elimina_usuario()                  #elimina clientes
                    elif info_clientes_menu == "3":
                        lista_info_cliente()                #info por cliente      
                    elif info_clientes_menu == "4":
                        solicitud_ingreso = False       #sale del menu
                    else:
                        print("Opción no válida")





