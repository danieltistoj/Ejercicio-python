class Email: 
    def __init__(self):
        self.enviado = False
    def enviar_correo(self):
        self.enviado=True

mi_correo = Email()
print(mi_correo.enviado)#Envia false
mi_correo.enviar_correo()#Se modifica el atributo con el metodo
print(mi_correo.enviado)#Envia true
