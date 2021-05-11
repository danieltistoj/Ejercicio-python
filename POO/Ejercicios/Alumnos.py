#Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno
#Definir los metodos para inicializar sus atributos, imprimirlos y mostrar con el resultado de la nota y si ha aprobado o no
class Alumno:
    #Este es un constructor
    def __init__(self):
        self.nombre = input("Nombre del alumno: ")
        self.nota = float(input("Nota del alumno: "))
    def notaAlumno(self):
        print("Alumno:",self.nombre)
        print("Nota:",self.nota)
    def resultadoNota(self):
        if self.nota<5:
            print("El alumno ha reprobado")
        else:
            print("El alumno ha aprobado")

alumno1 = Alumno()
alumno2 = Alumno()

alumno1.notaAlumno()
alumno1.resultadoNota()
print("")
alumno2.notaAlumno()
alumno2.resultadoNota()
