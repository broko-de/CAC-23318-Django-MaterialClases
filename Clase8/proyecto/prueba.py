from recursos_humanos.nomina import Nomina
from recursos_humanos.personal.estudiantes import Estudiante
from recursos_humanos.personal.empleados import Empleado, EmpleadoFullTime, EmpleadoPorHora



nomina_empleados = Nomina()
nomina_empleados.__lista_empleados = [1,32]

nomina_empleados.agregar_empleado(EmpleadoFullTime('Mario', 'Lobo', 6000))
nomina_empleados.agregar_empleado(EmpleadoFullTime('Daniel', 'Juarez', 6500))
nomina_empleados.agregar_empleado(EmpleadoPorHora('Gutavo', 'Balvorin', 200, 50))
franco_sosa = EmpleadoPorHora('Franco','Sosa',150,100)
nomina_empleados.agregar_empleado(franco_sosa)
nomina_empleados.agregar_empleado(EmpleadoPorHora('Santi', 'Caseres', 100, 150))
print(nomina_empleados.print())