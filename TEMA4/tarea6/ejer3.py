diccionario={}
diccionario['CastellanoBuenosDias']='Buenos dias'
diccionario['CastellanoBuenasNoches']='Buenas noches'
diccionario['CastellanoHola']='Hola'
diccionario['CastellanoAdios']='Adios'

diccionario['InglesBuenosDias']='Good morning'
diccionario['InglesBuenasNoches']='Good night'
diccionario['InglesHola']='Hellow'
diccionario['InglesAdios']='Bye'


idioma=input('Escoge idioma')
frase=input('Escoge frase')

print(diccionario[idioma+frase])