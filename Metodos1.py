class Matematica:
    def suma(self):#self esa una referencia en un determinado objeto, un objeto que aun no se a creado
        self.n1 = 2
        self.n2 = 3

s = Matematica()
s.suma()
print(s.n1 + s.n2)
#suma y pinta =  5

