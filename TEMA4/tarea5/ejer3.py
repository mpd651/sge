cadena = input('Introduce una cadena: ')

palabras= cadena.split(' ')
for i in palabras:
    print(i[0], end='')

print('')
for i in palabras:
    print(i.capitalize(), end =' ')

print('')
for i in palabras:
    if i.startswith('A') or i.startswith('a'):
        print(i, end=", ")