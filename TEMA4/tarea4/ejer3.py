lista = ['hola', 'que', 'tal']

print('Escribe algo que este en la lista')
cadena=input()
contador=0

for i in lista:
    if i==cadena:
        contador=contador+1

print(f'la palabra {cadena} aparece {lista.count(cadena)} veces')

print('Escribe algo para sustituir en la lista')
sustituidor=input()
lista[lista.index(cadena)]=sustituidor
print(lista[lista.index(sustituidor)])



