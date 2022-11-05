class Coche:
    def __init__(self,marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.arrancado = False
    def arrancar(self):
        self.arrancado= True
        print("El",self.marca, self.modelo,"Se ha arrancado")
    def parar(self):
        self.arrancado = False
        print("El", self.marca, self.modelo, "Se ha detenido")


laguna = Coche("Renault","Laguna")
tesla = Coche("Tesla","Model 3")

print(laguna.marca, laguna.modelo)
print(tesla.marca, tesla.modelo)

laguna.arrancar()
tesla.parar()






