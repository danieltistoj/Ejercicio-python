class Auto:
    Rojo = False

    def __init__(self,puertas=None,color=None):
        self.puertas = puertas
        self.color = color
        if puertas is not None and color is not None:
            print("Se creo un auto con puerts {} y color {}".format(puertas, color))
    def Fabricar(self):
        self.Rojo = True
    def confirmar_fabricacion(self):
        if(self.Rojo):
            print("auto color rojo")
        else:
            print("auto no esta coloreado")

auto = Auto(2,"rojo")
auto.confirmar_fabricacion()
auto.Fabricar()
auto.confirmar_fabricacion()
print("Color rojo:",auto.Rojo)