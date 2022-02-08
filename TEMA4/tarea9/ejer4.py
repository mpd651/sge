class calculadora():
    def __init__(self, num1, num2):
        self._num1=num1
        self._num2=num2
    
    def suma(self):
        print(f'La suma es {self._num1+self._num2}')
    
    def resta(self):
        print( f'La resta es {self._num1-self._num2}')

    def multiplicacion(self):
        print(f'La multiplicacion es {self._num1*self._num2}')

    def division(self):
        print(f'La division es {self._num1/self._num2}')

c=calculadora(5,4)
c.suma()
c.resta()
c.multiplicacion()
c.division()