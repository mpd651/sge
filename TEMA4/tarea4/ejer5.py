lista = []

for i in range (1900, 2200):
    if i%4 == 0 and (i%100 != 0 or i%400==0):
        lista.append(i)
        print(i, end=" ")

numero= int(input('\n Introduce un año: '))
if numero in lista:
    print(f'el año {numero} es bisiesto')
else:
    print('No es bisiesto')