#####################################################################
# Clases                                                            #
#####################################################################
#                                                                   #
#   Sintaxis: class [nombre de la clase]):                          #
#                                                                   #
#   Ejemplos:                                                       #
#       class Alumno:                                               #    
#                                                                   #
#####################################################################

from datetime import datetime

#Creamos una clase utilizando class
class Alumno:
    #Variables o Propiedades de la clase
    Nombre = None
    Apellido1 = None
    Apellido2 = None
    FechaNacimiento = None

    #Función constructor se ejecuta al crear el objeto
    #self represente al mismo objeto
    def __init__(self, nombre, apell1, apell2) -> None:
        self.Nombre = nombre
        self.Apellido1 = apell1
        self.Apellido2 = apell2

    def getNombreCompleto(self) -> str:
        return f"{self.Nombre} {self.Apellido1} {self.Apellido2}"

    def setFechaNacimiento(self, fecha) -> bool:
        try:
            if(len(fecha) == 8):
                self.FechaNacimiento = datetime.strptime(fecha, "%d-%m-%y").date()
            else:
                self.FechaNacimiento = datetime.strptime(fecha, "%d-%m-%Y").date()

            return True           
        except:
            return False

    def getEdad(self) -> int:
        if (self.FechaNacimiento == None): 
            return -1
        else:
            return datetime.now().year - self.FechaNacimiento.year


#Instanciamos el Objeto, se ejecuta la función constructor
alumno = Alumno("Borja", "Cabeza", "Rozas")

print(f"Me llamo: {alumno.Nombre} {alumno.Apellido1} {alumno.Apellido2}")
print(f"Me llamo: {alumno.getNombreCompleto()}")

#Invocamos a las funciones del objeto
resultado = alumno.setFechaNacimiento("11-09-95")

if (resultado == True):
    print("Fecha asignada correctamente")
else:
    print("Error al asignar fecha")

#alumno.setFechaNacimiento(input("Dime tu fecha de nacimiento: "))

#fecha = input("Dime tu fecha de nacimiento: ")
#alumno.setFechaNacimiento(fecha)

if(alumno.getEdad() == -1):
    print("La edad no se puede calcular")
else:
    print(f"Edad: {alumno.getEdad()} años")
