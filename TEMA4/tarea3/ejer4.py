import math
from random import Random, randint, random


print('jugador 1 Quieres generar un numero del 1 al 6? (si/no)')
respuesta1=input()
print('jugador 2 Quieres generar un numero del 1 al 6? (si/no)')
respuesta2=input()
suma=0

while respuesta1=='si' and respuesta2=='si':
    num1=randint(1,6)
    num2=randint(1,6)
    suma=suma+num1

    if num1>num2:
        print(f'El primer dado es mayor ha sacado un {num1} frente a {num2}')
    elif num2>num1:
        print(f'El segundo dado es mayor ha sacado un {num2}, frente a {num1}')
    elif num1==num2:
        print(f'Los dos dados han dado el mismo resultado. {num1},{num2}')
    print('jugador 1 Quieres generar un numero del 1 al 6? (si/no)')
    respuesta1=input()
    print('juegador 2 Quieres generar un numero del 1 al 6? (si/no)')
    respuesta2=input()


print('uno de los dos jugadores no ha querido seguir jugando')

print(f'la suma de los numeros es {suma}')
print ('programa finalizado')
