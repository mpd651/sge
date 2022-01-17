print('Introduce un numero: ')
num=int(input())
contador=0

for i in range (1, num+1):
    if num%i==0:
        contador=contador+1

if contador==2:
    print(f'El numero {num} es primo')
else:
    print('No es primo')