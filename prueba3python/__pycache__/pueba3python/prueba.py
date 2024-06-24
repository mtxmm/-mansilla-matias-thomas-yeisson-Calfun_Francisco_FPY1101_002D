import funciones as funcion
libros=[]
libro=[]
while True:
    print("--menu de opciones")
    print("""
        1.-agregar libro
        2.-ver libros
        3.-modificar libros
        4.-eliminar libros
        5.-guardar coleccion
        6.-salir del programa
    

    """)
    try:
        opcion=int(input("ingresar opcion: "))
    except ValueError:
        print("debe ingresar un numero")
    else:
        if opcion==1:
            funcion.agregarLibros()
        elif opcion==2:
            funcion.verLibros()
        elif opcion==3:
            print("modificar libro")
        elif opcion==4:
            funcion.eliminarlibro()
            
        elif opcion==5:
            funcion.guardar_archivo()
            
