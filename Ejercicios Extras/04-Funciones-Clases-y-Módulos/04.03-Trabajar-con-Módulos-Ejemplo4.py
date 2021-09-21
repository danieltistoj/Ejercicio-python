import sys
sys.path.insert(0, '..\\python\\Modulos')

# Importamos un objeto de un módulo y utilizamo AS para crear un alias
from GestionEscuela import Alumno as FichaAlumno

alumno = FichaAlumno("Ana", "Sánchez", "Sanz")

print(f"Me llamo: {alumno.Nombre} {alumno.Apellido1} {alumno.Apellido2}")
print(f"Me llamo: {alumno.getNombreCompleto()}")