import os

def funcionLeerEscribir (ficheroNombre):
    with open(ficheroNombre, "a+") as fichero:
        print('Desea editar el archivo?(salir)')
        opcion=input()
        while opcion!='salir':
            print('Introduce texto a concateear en el fichero:')
            texto=input()
            fichero.write("\n")
            fichero.write(texto)
            print('Desea editar el archivo?(salir):')
            opcion=input()
        contenido=fichero.read()
        print (contenido)
    fichero.closed

if __name__=="__main__":
    print('Introduce un nombre de fichero: ')
    ficheroNombre=input()
    if os.path.exists(ficheroNombre):
        funcionLeerEscribir (ficheroNombre)

    else:
        print('El fichero no existe')
        funcionLeerEscribir (ficheroNombre)







