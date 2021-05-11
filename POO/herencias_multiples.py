class Primera:
    def __init__(self):
        print("Yo soy la primera clase")
    def primera(self):
        print("Este es el metodo heredado de Primera")

class Segunda:
    def __init__(self):
        print("Yo soy la segunda clase")
    def segunda(self):
        print("Este es el metodo heredado de Segunda")

class Tercera(Primera,Segunda):
    def tercera(self):
        print("Este es el metodo heredado de Tercera")

herencia_multiple = Tercera()
herencia_multiple.primera()
herencia_multiple.segunda()
herencia_multiple.tercera()

