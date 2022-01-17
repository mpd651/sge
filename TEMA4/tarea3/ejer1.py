print('Introduce un numero:')
num=int(input())
multiplicador=0

while multiplicador<=10:
    print (f'{num}*{multiplicador}={num*multiplicador}')
    multiplicador=multiplicador+1

for i in range (11):
    print (f'{num}*{i}={num*i}')
