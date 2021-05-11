class Fabrica:
    def __init__(self,tiempo,nombre,ruedas):
        self.tiempo = tiempo
        self.nombre = nombre
        self.ruedas = ruedas
        print("Se creo el auto",self.nombre)
    def __del__(self):
        print("Se elimino el auto")
    def __str__(self):
        return "{} se fabrico con exito, en el tiempo {} y tiene la cantidad de ruedas {}".format(self.nombre,self.tiempo,self.ruedas)
    def __len__(self):
        return self.tiempo

a = Fabrica(10,"Estudiante",4)
print(str(a))
print(len(a))
