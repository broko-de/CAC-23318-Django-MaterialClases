from abc import ABC, abstractmethod


class Persona(ABC):

    def __init__(self,nombre,apellido,dni,email):
        self.__nombre = nombre
        self._apellido = apellido
        self.dni = dni        
        self.email = email
    
    def __str__(self):
        return f'{self.apellido}, {self.nombre}'


    @abstractmethod
    def registrarse(self):
        pass

    #GETTER
    @property
    def pepe(self):
        return self.__nombre
    
    #SETTER
    @pepe.setter
    def pepe(self,nuevo_nombre):
        self.__nombre = nuevo_nombre

    #


class Estudiante(Persona):

    def __init__(self, nombre, apellido, dni, email,matricula):
        super().__init__(nombre, apellido, dni, email)
        self.matricula = matricula

    def registrarse(self):
        return f'El estudiante {self.apellido} se registro exitosamente'
    

class Docente(Persona):

    def __init__(self, nombre, apellido, dni, email,legajo):
        super().__init__(nombre, apellido, dni, email)
        self.legajo = legajo
    
    def registrarse(self):
        return f'Docente registrado con exito!'
    

estudiante_uno = Estudiante('Jose','Argento',34111222,'pepe@gmail.com','LM-2333')
print(estudiante_uno.pepe)
estudiante_uno.pepe = 'Rogelio'
print(estudiante_uno.pepe)
# print(estudiante_uno._apellido)

# docente_uno = Docente('Mony','Argento',3434333,'moni@gmail.com','DC23232')
# print(docente_uno.registrarse())

