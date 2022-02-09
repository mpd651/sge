diccionario={}

diccionario['uno']=1
diccionario['uno.2']=1
diccionario['dos']=2
diccionario['tres']=3
i=diccionario.items()
print(i)

lista=[]
for i in diccionario.values():
    if i not in lista:
        lista.append(i)

print(lista)