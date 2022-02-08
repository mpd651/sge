class pelicula():
    def __init__(self, titulo, duracion, anio):
        self._titulo=titulo
        self._duracion=duracion
        self._anio=anio

    def info_pelicula(self):
        return f'Titulo: {self._titulo}, duracion: {self._duracion}, anio: {self._anio}'

class catalogo():
    def __init__(self, peliculas):
        self._peliculas=list(peliculas)
        
    def agregar(self, pelicula):
        self._peliculas.append(pelicula)

    def mostrarDatos(self):
        for obj in self._peliculas:
            print(obj.info_pelicula())

p1=pelicula("titulo1", 20, 2000)
p2=pelicula("titulo2", 25, 2010)
p3=pelicula("titulo3", 30, 2020)

peliculas=[p1, p2, p3]
c=catalogo(peliculas)
c.mostrarDatos()


