#! /usr/bin/python3
print('Introduce un año:')
anio=int(input())

if anio%4==0 and (anio%100!=0 or anio%400==0):
    print('El año es bisiesto')
else:
    print('El año no es bisiesto')