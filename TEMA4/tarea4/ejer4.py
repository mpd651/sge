lista=[1,2,3,4,5]
copia=lista[:]

copia.sort()

if lista==copia:
    print(f'las listas son iguales, estan ordenadas')
else:
    print(f'Las listas no son iguales')
