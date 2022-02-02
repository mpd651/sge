class Persona():
    def __init__(self):
        _nombre=''
        _edad=0

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre=nombre
    
    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad=edad

    def __str__(self):
        return 'Nombre: '+self.nombre+', edad: '+str(self.edad)
    
    def mayorEdad(self):
        if self._edad>=18:
            return 'Es mayor de edad'
        else:
            return 'Es menor'

    
