print('Escribe una frase: ')
cadena=input()

palabras=cadena.split(" ")

diccionario = {}

for i in palabras:
    diccionario[i]=cadena.count(i)

print(diccionario)

