from django.db import models

#Modelo UNICO - SOLUCION 1
# class Persona(models.Model):
#     nombre = models.CharField(max_length=100,verbose_name='Nombre')
#     apellido = models.CharField(max_length=150,verbose_name='Apellido')
#     email = models.EmailField(max_length=150,null=True)
#     dni = models.IntegerField(verbose_name="DNI")
#     matricula = models.CharField(max_length=10,verbose_name='Matricula',null=True)
#     baja = models.BooleanField(default=0,null=True)
#     legajo = models.CharField(max_length=10,verbose_name='Legajo',null=True)

#Modelo Abtracto - SOLUCION 2
# class PersonaAbs(models.Model):
#     nombre = models.CharField(max_length=100,verbose_name='Nombre')
#     apellido = models.CharField(max_length=150,verbose_name='Apellido')
#     email = models.EmailField(max_length=150,null=True)
#     dni = models.IntegerField(verbose_name="DNI")

#     class Meta:
#         abstract=True

# class EstudianteAbs(PersonaAbs):
#     matricula = models.CharField(max_length=10,verbose_name='Matricula')

# class InstructorAbs(PersonaAbs):
#     legajo = models.CharField(max_length=10,verbose_name='Legajo')

#HERENCIA - SOLUCION 3
# class Persona(models.Model):
#     nombre = models.CharField(max_length=100,verbose_name='Nombre')
#     apellido = models.CharField(max_length=150,verbose_name='Apellido')
#     email = models.EmailField(max_length=150,null=True)
#     dni = models.IntegerField(verbose_name="DNI")

# class Estudiante(Persona):
#     matricula = models.CharField(max_length=10,verbose_name='Matricula')
#     baja = models.BooleanField(default=0)

#     def __str__(self):
#         return f"{self.matricula} - {self.nombre} {self.apellido}"
    
#     def soft_delete(self):
#         self.baja=True
#         super().save()
    
#     def restore(self):
#         self.baja=False
#         super().save()
    
#     class Meta():
#         verbose_name_plural = 'Estudiantes'

# class Instructor(Persona):
#     legajo = models.CharField(max_length=10,verbose_name='Legajo')

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    descripcion = models.TextField(null=True,verbose_name='Descripcion')
    baja = models.BooleanField(default=0)

    def __str__(self):
        return self.nombre

    def soft_delete(self):
        self.baja=True
        super().save()
    
    def restore(self):
        self.baja=False
        super().save()

class Curso(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    descripcion = models.TextField(null=True,verbose_name='Descripcion')
    fecha_inicio = models.DateField(verbose_name='Fecha de inicio',null=True,default=None)
    portada = models.ImageField(upload_to='imagenes/',null=True,verbose_name='Portada')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE) #relacion mucho a uno    

    def __str__(self):
        return self.nombre
    
    def delete(self,using=None,keep_parents=False):
        self.portada.storage.delete(self.portada.name) #borrado fisico
        super().delete()

class Comision(models.Model):
    nombre = models.CharField(max_length=100,verbose_name="Nombre")
    horario = models.CharField(verbose_name="Horario",null=True,default=None)
    link_meet = models.URLField(max_length=100,verbose_name='Link de Meet')
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE) #relacion mucho a uno
