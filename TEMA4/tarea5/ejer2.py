from unicodedata import digit


print('Introduce una cadena')
cadena=input()

print('Introduce un caracter')
caracter=input()

for i in range (0, 10):
    cadena=cadena.replace(str(i), caracter)

print(cadena)
