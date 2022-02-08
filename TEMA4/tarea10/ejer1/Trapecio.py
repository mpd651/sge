


from Figura import Figura


class Trapecio(Figura):
    def __init__(self, base, altura, base_2):
        super().__init__(base, altura)
        self._base2=base_2

    def area(self):
        return (self._base+self._base2)/2*self._altura

    def info_figura (self):
        print(f'Base: {self.base}, Base2: {self._base2}, Altura: {self.altura}, Area: {self.area()}')