class cliente():
    def __init__(self, nombre, cantidad):
        self._nombre=nombre
        self._cantidad=cantidad

    @property
    def cantidad(self):
        return self._cantidad

    def depositar(self, cantidad):
        self._cantidad=self._cantidad+cantidad

    def extraer (self, cantidad):
        if self._cantidad-cantidad>=0:
            self._cantidad=self._cantidad-cantidad
        else:
            print('No se puede extraer tanto dinero')
    
    def mostrar_total(self):
        print (f'Cliente: {self._nombre}, cantidad: {self._cantidad}')


class banco():
    def __init__(self, cliente1, cliente2, cliente3):
        self._cliente1=cliente1
        self._cliente2=cliente2
        self._cliente3=cliente3

    def deposito_total(self):
        return self._cliente1.cantidad + self._cliente2.cantidad + self._cliente3.cantidad

c1=cliente("mario", 50)
c2=cliente("juan", 100)
c3=cliente("laura", 50)

b=banco(c1, c2, c3)
print(b.deposito_total())
c1.mostrar_total()
c2.mostrar_total()
c3.mostrar_total()


