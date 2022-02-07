class Figura():
    def __init__(self, base=6 , altura=4):
        self._base=base
        self._altura=altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        self._base=base

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        self._altura=altura

    def area(self):
        return self.base*self.altura

    def ifo_figura (self):
        print(f'Base: {self.base}, Altura: {self.altura}, Area: {self.area}')
        
    
     