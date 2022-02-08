from operator import truediv


class vehiculo():
    def __init__(self, marca, modelo, ):
        self.marca=marca
        self.modelo=modelo
        self.arrancando=False
        self.acelerando=False
        self.frenando=False

    def frenar(self):
        self.frenando=True

    def acelerar(self):
        self.acelerando=True

    def arrancar(self):
        self.arrancando=True

    def estado(self):
        print (f'Vehiculo de marca {self.marca}, modelo {self.modelo}, esta arrancando {self.arrancando}, esta frenando {self.frenando}, esta acelerando {self.acelerando}')

class vehiculoElectrico():
    def init(self):
        self.autonomia=300
    
    def cargarBateria(self):
        return False

    def estado_bateria(self):
        print(f'Vehiculo electrico, bateria: {self.autonomia}, bateria cargando: {self.cargarBateria()}')

class avion(vehiculo):
    def tipo(self, nmotores):
        self.nmotores=nmotores
    
    def estado(self):
        print(f'Avion: {super().estado()}, numero de motores: {self.nmotores}')

v=vehiculo('Airbus', 335)
v.estado()


