import sys
sys.path.insert(0, '..\\python\\Modulos')

# Importamos todo el contenido de un módulo
# Tenemos que utilizar el nombre del Módulo para acceder a sus objetos o funciones
import GestionEscuela

alumno = GestionEscuela.Alumno("Ana", "Sánchez", "Sanz")

print(f"Me llamo: {alumno.Nombre} {alumno.Apellido1} {alumno.Apellido2}")
print(f"Me llamo: {alumno.getNombreCompleto()}")