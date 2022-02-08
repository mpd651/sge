from inspect import Parameter
from mailbox import NoSuchMailboxError



class contacto():
    def __init__(self, nombre, telefono, email):
        self._nombre=nombre
        self._telefono=telefono
        self._email=email
    
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre=nombre

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, telefono):
        self._telefono=telefono
    
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email=email

    def infoContacto(self):
        return f'Nombre: {self._nombre}, telefono: {self._telefono}, email: {self._email}'

class agenda():
    def __init__(self):
        self._contactos=[]
    
    def anadirContacto(self, contacto):
        self._contactos.append(contacto)

    def listaContactos(self):
        for obj in self._contactos:
            print(f'Nombre: {obj.nombre()}, telefono: {obj.telefono()}, email: {obj.email()}')

    def buscarContacto(self, nombre):
        for c in self._contactos:
            if c.nombre() == nombre:
                print(f'Contacto encontrado, nombre: {c.nombre()}, posicion en la lista {self._contactos.index(contacto)}')

    def editarContacto(self, nombre):
        for c in self._contactos:
            if c.nombre()==nombre:
                print('1-editar nombre\n 2-editar telefono\n 3-editar email\n')
                opcion=int(input('Introduce una opcion:'))
                
                if opcion==1:
                    nombre=input('Introduce un nombre:')
                    c.nombre(nombre)

                elif opcion==2:
                    telefono=int(input('Introduce un telefono:'))
                    c.telefono(telefono)

                elif opcion==3:
                    email=input('Introduce un email:')
                    c.email(email)

    def menuAgenda(self):
        print('Menu:')
        print('1-Anadir Contacto\n 2-Lista de contactos\n 3-Buscar contacto\n 4-Editar contacto\n 0-Salir')
        opcion=int(input('Introduzca una opcion'))

        while (opcion!=0):
            if opcion==1:
                c=contacto(input('Introduce nombre:'), input('Introduce telefono:'), input('Introduce email'))
                self.anadirContacto(c)
            
            elif opcion==2:
                self.listaContactos()

            elif opcion==3:
                nombre=input('Introduce un nombre')
                self.buscarContacto(nombre)

            elif opcion==4:
                nombre=input('Introduce un nombre')
                self.editarContacto()

            print('Menu:')
            print('1-Anadir Contacto\n 2-Lista de contactos\n 3-Buscar contacto\n 4-Editar contacto\n 0-Salir')
            opcion=int(input('Introduzca una opcion'))

a=agenda()
a.menuAgenda()



