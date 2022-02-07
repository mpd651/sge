from ejer1.Figura import Figura


class Triangulo(Figura):
    def __init__(self, base, altura):
        super().__init__(base, altura)
    
    def area(self):
        return self._base*self._altura/2
    
    