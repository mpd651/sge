from unicodedata import digit


print('Introduce una cadena')
cadena=list(input())

print('Introduce un caracter')
caracter=input()

for i in range (len(cadena)):
    cadena=cadena.replace(cadena[i], caracter)

print(cadena)
