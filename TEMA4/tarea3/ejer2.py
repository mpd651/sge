print('Introduce un numero:')
num=int(input())

contador=1
factorial=1
#while contador<num:
#    factorial=factorial+(contador*factorial)
#    contador=contador+1
    
for i in range(1, num):
    factorial=factorial+(i*factorial)

print(f'El factorial es {factorial}')
