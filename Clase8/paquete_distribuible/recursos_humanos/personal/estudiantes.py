from recursos_humanos.personal.empleados import Empleado

#Herencia múltiple
class Estudiante():
    def __init__(self, legajo):
        self.legajo = legajo

    @property
    def legajo(self):
        return self.__legajo

    #falta setter
    @legajo.setter
    def legajo(self, legajo_nuevo):        
        self.__legajo = legajo_nuevo

    def __str__(self):
        return f"Legajo: {self.__legajo}"


class EstudiantePasante(Estudiante, Empleado):
    def __init__(self, nombre, apellido, legajo):
        Empleado.__init__(self, nombre, apellido)
        Estudiante.__init__(self, legajo)

    # Tengo que implementar la propiedad salario porque hereda de empleado
    @property
    def salario(self):
        return 0

    def __str__(self):
        return f"{self.nombre_completo}. Legajo: {self.legajo}"
    
    def hola(self):
        print('Hola')