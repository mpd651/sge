


from Figura import Figura


class Triangulo(Figura):
    def __init__(self, base, altura):
        super().__init__(base, altura)
    
    def area(self):
        return self._base*self._altura/2

    def info_figura (self):
        print(f'Base: {self.base}, Altura: {self.altura}, Area: {self.area()}')
    
    