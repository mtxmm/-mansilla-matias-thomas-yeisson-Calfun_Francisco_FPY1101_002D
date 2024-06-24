libros=[]


def agregarLibros():
    titulo=input("ingresar titulo: ")
    autor=input("ingresar autor:")
    año_publicacion=int(input("ingresar año de publicacion: "))
    genero=input("ingresar genero(fantasia- infantil-ciencia ficcion):")


    libro={
        "titulo":titulo,
        "autor":autor,
        "año_publicacion":año_publicacion,
        "genero":genero
        }
    
    libros.append(libro)
    print("el  se agrego de forma exitosa")


def verLibros():
    print("mostrando libros")
    print(f"--{libros}")

def modificarlibro():
    print()

def eliminarlibro():
    input("ingresar que libro eliminar: ")
    

     


def guardar_archivo():
    print("1.-imprimir libros")
    print("2.-imprimir un solo libro")
    try:
        opcion=int(input("ingresar un opcion: "))
    except ValueError:
        print("debe ingresar un numero")
    else:
        if opcion==1:
            with open('plantilla_libros.txt', 'w') as archivo:
                for libro in libros:
                    archivo.write(f"{libro['titulo']} / autor:{libro['autor']} / año de publicacion:{libro['año_publicacion']} / genero:{libro['genero']}  \n")
            print("se imprimio 'plantilla_libros.txt' ")
        elif opcion==2:
            genero=input("ingresar genero(fantasia - infantil- ciencia fincion): ")
            with open(f'libro_{genero}.txt', 'w') as archivo:
                for libro in libros:
                    if libro['genero'] ==genero.lower():
                        archivo.write(f"{libro['titulo']} / autor:{libro['autor']} / año de publicacion:{libro['año_publicacion']} / genero:{libro['genero']}  \n")

            print(f"el libro {libro} se imprimio en 'libro_{libro}.txt' ")






