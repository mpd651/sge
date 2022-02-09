print('Introduce el nombre de una persona: (* para salir)')
persona=input()
print('Introduce una aficcion de la persona')
aficcion=input()
diccionario={}
gustos=[]


while (persona!="*"):
    if persona not in diccionario:
        gustos=[]
        gustos.append(aficcion)
        diccionario[persona]=gustos
    else:
        gustos=diccionario[persona]
        encontrado=False
        for i in gustos:
            if i==aficcion:
                print('La persona ya tiene esa aficcion')
                encontrado=True
        if encontrado==False:
            gustos.append(aficcion)
            diccionario[persona]=gustos
    print('Introduce el nombre de una persona: (* para salir)')
    persona=input()
    print('Introduce una aficcion de la persona')
    aficcion=input()

print(diccionario)