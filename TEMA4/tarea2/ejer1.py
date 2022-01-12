#! /usr/bin/python3
print('Introduce numero a')
a=int(input())
print('Introduce numero b')
b=int(input())

suma=a+b
if suma>0:
    print('la suma es mayor que 0')
elif suma==0:
    print('la suma es 0')
elif suma<0:
    print('la suma es menor que 0')