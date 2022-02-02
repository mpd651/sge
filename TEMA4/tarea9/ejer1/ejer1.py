class Alumno():
    def __init__(self, nombre='Mario', nota=8):
        self._nombre=nombre
        self._nota=nota
    
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre=nombre

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, nota):
        if nota>=0 and nota<=10:
            self._nota=nota
        else:
            raise ValueError("Nota entre 0 y 10")
            self._nota=0
    
    def __str__(self):
        mensaje='Nombre: '+self.nombre +', Nota: '+ str(self.nota)
        return mensaje

    def evaluar(self):
        if self.nota>=5:
            return 'Nombre: '+self.nombre+' ha sacado un '+str(self.nota)+', HA APROBADO'
        else:
            return 'Nombre: '+self.nombre+' ha sacado un '+str(self.nota)+', HA SUSPENDIDO'

a=Alumno()
print(a)
cadena=a.evaluar()
print(cadena)