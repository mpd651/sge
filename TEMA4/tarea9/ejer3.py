class Triangulo():
    def __init__(self, lado1, lado2, lado3):
        self._lado1=lado1
        self._lado2=lado2
        self._lado3=lado3

    def ladoMayorYTipo(self):
        if (self._lado1>self._lado2 and self._lado1>self._lado3):
            print('El lado 1 es mayor')
        elif (self._lado2>self._lado1 and self._lado2>self._lado3):
            print('El lado 2 es mayor')
        elif (self._lado3>self._lado1 and self._lado3>self._lado2):
            print('El lado 3 es mayor')
        
        if (self._lado1==self._lado2 and self._lado2==self._lado3):
            print('El triangulo es equilatero')
        elif (self._lado1==self._lado2 or self._lado2==self._lado3 or self._lado1==self._lado3):
            print('El triangulo es isosceles')
        else:
            print('El triangulo es escaleno')
    
t=Triangulo(4, 4, 4)
t2 =Triangulo (5, 5 ,4)
t3=Triangulo(4,5,6)

t.ladoMayorYTipo()
t2.ladoMayorYTipo()
t3.ladoMayorYTipo()

    
    