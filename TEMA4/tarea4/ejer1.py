print('Introduce un numero')

num=int(input())
lista=[]
while num>=0:
    lista.append(num)
    print('Introduce otro numero')
    num=int(input())

print('PARES')
for i in lista:
    if i%2==0:
        print(i)

print(f'MAXIMO {max(lista)}')
