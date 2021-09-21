import sys
sys.path.insert(0, '..\\python\\Modulos')

# Importamos todas funciones y objeto de un módulo utilizando *
from GestionEscuela import *

alumno = Alumno("Ana", "Sánchez", "Sanz")

print(f"Me llamo: {alumno.Nombre} {alumno.Apellido1} {alumno.Apellido2}")
print(f"Me llamo: {alumno.getNombreCompleto()}")