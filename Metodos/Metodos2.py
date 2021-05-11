#metodos II
class Ropa:
    def __init__(self):
        self.marca = 'willow'
        self.talla = 'M'
        self.color = 'rojo'

camisa = Ropa()
print(camisa.talla)
print(camisa.marca)

class Calculadora:
    def __init__(self,n1,n2): #este tipo de metodo es un constructor
        self.suma = n1 + n2
        self.resta = n1-n2
        self.producto = n1*n2
        self.division = n1/n2

operacion = Calculadora(2,3)#Se le deben de mandar los parametros del constructor 
print(operacion.producto)
print(operacion.suma)
print(operacion.resta)
