
from youtube_dl import main
from Trapecio import Trapecio

from Triangulo import Triangulo


def main():
    triangulo= Triangulo(6, 4)
    print(triangulo.area())
    triangulo.info_figura()

    trapecio=Trapecio(6, 4, 4)
    trapecio.info_figura()

if __name__=="__main__":
    main()
