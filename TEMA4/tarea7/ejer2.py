import csv
import json
import os


print('MENU:')
print('1 Listar datos\n2 Crear contacto\n3 Borrar contacto\n4 Guardar CSV\n5 Guardar JSON\n6 Cargar CSV\n7 Cargar JSON\n 0 Salir')
opcion=int(input('Introduce una opcion'))
contactos=[]

while opcion!=0:
    if opcion==1:
        for i in contactos:
            print(i)
            print("\n")

    if opcion==2:
        print('Introduce el nombre:')
        nombre=input()
        print('Introduce telefono')
        telefono=input()
        print('Introduce direccion:')
        direccion=input()
        contacto=[nombre, telefono, direccion]
        contactos.append(contacto)

    if opcion==3:
        print('Introduce nombre de contacto a borrar:')
        nombre=input()
        indice =0
        indiceBorrado=0
        for i in contactos:
            if i[0]==nombre:
                indiceBorrado=indice
            indice=indice+1
        contactos.pop(indiceBorrado)
                
        
    if opcion==4:
        print('Introduce nombre del fichero a guardar CSV:')
        nombre=input()
        with open (nombre+'.csv', 'w') as fichero:
            escritor=csv.writer(fichero)
            escritor.writerows(contactos)
        print('fichero guardado')

    if opcion==5:
        print('Introduce nombre del fichero a guardar JSON:')
        nombre=input()
        fichero=open(nombre+'.json', 'w')
        json.dump(contactos,fichero)
        fichero.close()
        print('fichero guardado')

    if opcion==6:
        print('Introduce nombre del fichero a leer CSV:')
        nombre=input()
        
        if os.path.exists(nombre+'.csv'):
            with open (nombre+'.csv') as fichero:
                lector=csv.reader(fichero)
                listaContenido=list(lector)
                for fila in listaContenido:
                    print (str(fila))
        else:
            print('El fichero no existe')

    if opcion==7:
        print('Introduce nombre del fichero a leer JSON:')
        nombre=input()
        if os.path.exists(nombre+'.json'):
            with open(nombre+'.json') as fichero:
                datos=json.load(fichero)
            for i in datos:
                print (i)
        else:
            print('El fichero no existe')
        
    
    print('MENU:')
    print('1 Listar datos\n2 Crear contacto\n3 Borrar contacto\n4 Guardar CSV\n5 Guardar JSON\n6 Cargar CSV\n7 Cargar JSON\n 0 Salir')
    opcion=int(input())
print('fin')
