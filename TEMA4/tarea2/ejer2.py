#! /usr/bin/python3
print('Introduce un numero de mes (entre 1 y 12): ')
mes=int(input())

if (mes%2!=0):
    print('dias: 31')
elif(mes==2):
    print('dias: 28')
elif (mes%2==0 and mes!=2):
    print('dias: 30')

if (mes==1):
    print('Enero, 31 dias')
elif (mes==2):
    print('Febrero, 28 dias')
elif (mes==3):
    print('Marzo, 31 dias')
elif (mes==4):
    print('Abril, 30 dias')
elif (mes==5):
    print('Mayo, 31 dias')
elif (mes==6):
    print('Junio, 30 dias')
elif (mes==7):
    print('Julio, 31 dias')
elif (mes==8):
    print('Agosto, 31 dias')
elif (mes==9):
    print('Septiembre, 30 dias')
elif (mes==10):
    print('Octubre, 31 dias')
elif (mes==11):
    print('Noviembre, 30 dias')
elif (mes==12):
    print('Diembre, 31 dias')

