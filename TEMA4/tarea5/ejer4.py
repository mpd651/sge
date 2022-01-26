cadena1=input('Introduce la primera cadena: ')
cadena2= input('Introduce la segunda cadena(mas pequeña que la anterior): ')

posicion=cadena1.find(cadena2)
if posicion>=0:
    print(f'la cadena {cadena2} esta contenida en {cadena1}')
else:
    print(f'la cadena {cadena2} NO esta contenida en {cadena1}')

if cadena1>cadena2:
    print(f'{cadena1} es mayor que {cadena2}')
else:
    print(f'{cadena2} es mayor que {cadena1}')