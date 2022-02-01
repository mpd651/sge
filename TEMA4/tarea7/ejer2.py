print('MENU:')
print('1 Listar datos\n2 Crear contacto\n3 Borrar contacto\n4 Guardar CSV\n5 Guardar JSON\n6 Cargar CSV\n7 Cargar JSON\n 0 Salir')
opcion=int(input())
contactos=list()

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
        continue
    if opcion==5:
        continue
    if opcion==6:
        continue
    if opcion==7:
        continue
    
    print('MENU:')
    print('1 Listar datos\n2 Crear contacto\n3 Borrar contacto\n4 Guardar CSV\n5 Guardar JSON\n6 Cargar CSV\n7 Cargar JSON\n 0 Salir')
    opcion=int(input())
print('fin')
