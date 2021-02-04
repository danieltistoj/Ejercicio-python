#Herencia
class Calculadora:
    def __init__(self,numero):
        self.n = numero
        self.dato =  [0 for  i in range(numero)]
    
    def ingresardato(self):
        self.dato = [int(input("Ingresar datos"+str(i+1))]
        
 
