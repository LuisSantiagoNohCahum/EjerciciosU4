import re 
#importamos libreria re
op=0
#para el menu usamos un while
while op !=6:
    print("\n==========================================")
    print("| Elija una opción de la lista            |\n")
    print("| 1.Variables válidas                     |")
    print("| 2.Enteros y decimales                   |")
    print("| 3.Expresiones aritméticas               |")
    print("| 4.Operadores condicionales              |")
    print("| 5.Cadenas de caracteres                 |")
    print("| 6.Salir del programa                    |")
    print("==========================================\n")
    op = int(input("Ingrese una opcion valida: "))
    
    if op==1:
        filename="prueba.rb"    #primero asignamos el archivo a leer
        textfile=open(filename,"r") #abrimos el archivo
        regex="[a-zA-Z]+[a-zA-Z0-9_]*\s?(?==|>)"    #declaramos la expresion regular
        reg=re.compile(regex)    #se la ER pasa a re.compile() como una cadena de caracteres.
        print("=======================VARIABLES VALIDAS HALLADAS=======================")
        var_rep=[]
        for linea in textfile:  #leemos el archivo linea por linea
            lista_temp=reg.findall(linea)   # buscamos las coincidencias en el archivo
            for i in range(0,len(lista_temp)): 
                var_rep.append(lista_temp[i])
                print(lista_temp[i])    #imprimimos las coincidencias encontradas en esa linea
        var_rep=list(set(var_rep))  #eliminamos las variables que se repiten para mostrar solo la lista de variables encontradas sin que se repitan
        print("\nLISTA DE VARIABLES SIN REPETIR\n"+str(var_rep)+"\n")
        textfile.close()    #cerramos el archivo
        print("==============================================================")
        
    elif op==2:
        filename="prueba.rb"     #primero asignamos el archivo a leer
        textfile=open(filename,"r")     #abrimos el archivo
        regex="(?<![a-z])\d{1,}\.?[\d]*"    #declaramos la expresion regular
        reg=re.compile(regex) #se la ER pasa a re.compile() como una cadena de caracteres.
        print("=======================ENTEROS Y DECIMALES HALLADOS=======================")
        for linea in textfile:      #leemos el archivo linea por linea
            lista_temp=reg.findall(linea)    # buscamos las coincidencias en el archivo
            for i in range(0,len(lista_temp)):
                print(lista_temp[i])    #imprimimos las coincidencias encontradas en esa linea
        textfile.close() 
        print("==============================================================")  
        
#como ya se comento las primeras dos opciones las demas lineas no son necesarias de comentar ya que se sigue el mismo procedimeinto
    elif op==3:
        filename="prueba.rb"
        textfile=open(filename,"r")
        regex="\w+\s*\=\s*\w+\s*[\+\-\*\/\%]+\s*\w+|[a-zA-Z0-9_\[\]]+\s*[\+\-\*\/\%]+\s*=\s*\w+"
        reg=re.compile(regex)
        print("=======================EXPRESIONES ARITMETICAS HALLADAS=======================")
        print("\n")
        for linea in textfile:
            lista_temp=reg.findall(linea)
            for i in range(0,len(lista_temp)):
                print(lista_temp[i])
        textfile.close()
        print("==============================================================") 
        
        

    elif op==4:
        filename="prueba.rb"
        textfile=open(filename,"r")
        regex="([a-zA-Z0-9_\[\]\.]+\s?)([<>!=][=]|[<>!]){1}(\s*[0-9a-zA-Z.\[\]]+)"
        reg=re.compile(regex)
        print("=======================OPERADORES CONDICIONALES HALLADOS=======================")
        for linea in textfile:
            lista_temp=reg.findall(linea)
            for i in range(0,len(lista_temp)):
                print(lista_temp[i])
        textfile.close
        print("==============================================================")  


    elif op==5:
        filename="prueba.rb"
        textfile=open(filename,"r")
        regex="\".*?\"|\'.*?\'"
        reg=re.compile(regex)
        print("=======================CADENAS DE CARACTERES=======================")  
        for linea in textfile:
            lista_temp=reg.findall(linea)
            for i in range(0,len(lista_temp)):
                print(lista_temp[i])
        textfile.close() 
        print("==============================================================")
        
    elif op<1 or op>6:
        print("Opción incorrecta, ingrese una opción valida nuevamente")
    else:
        print("Saliendo del programa...\n")
        print("----------PROGRAMA DESARROLLADO POR----------")
        print("Alumno: Luis Santiago Noh Cahum")
        print("Matricula: 19070049")
        print("Quinto semestre - A")
        print("Lenguajes y automatas 1 - Unidad 2")
        



