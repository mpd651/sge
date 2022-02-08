class monedero():
    def __init__(self, dineroInicial):
        self._dinero=dineroInicial

    def meterDinero(self, dinero):
        self._dinero=self._dinero+dinero
    
    def sacarDinero(self, dinero):
        if self._dinero-dinero>=0:
            self._dinero=self._dinero-dinero
        else:
            print('No puedes retirar tanto dinero')
    
    def consultarDinero(self):
        print(f'Dinero en la cuenta: {self._dinero}')

m=monedero(50)
m.sacarDinero(60)
m.sacarDinero(40)
m.consultarDinero()
m.meterDinero(20)
m.consultarDinero()
    