import sys
sys.path.insert(0, '..\\python\\Modulos')

# Importamos un objeto o función de un módulo
# Si queremos importar varios lo separamos por comas
from GestionEscuela import Alumno

alumno = Alumno("Ana", "Sánchez", "Sanz")

print(f"Me llamo: {alumno.Nombre} {alumno.Apellido1} {alumno.Apellido2}")
print(f"Me llamo: {alumno.getNombreCompleto()}")