print('Introduce una cadena')
cadena=list(input())
print('Introduce un caracter')
caracter=input()

nueva=caracter.join(cadena)



cadenaSeparador=""
contador=0
for i in cadena:
    cadenaSeparador=cadenaSeparador+cadena[contador]+caracter
    contador=contador+1

print (cadenaSeparador)