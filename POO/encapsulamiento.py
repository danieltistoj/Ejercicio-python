class encapsulamiento:
    __privado_atri = "soy un atrinuto privado"

    def __privado_met(self):
        print("soy un metodo privado")
    def publico_atri(self):
        return self.__privado_atri
    def publico_met(self):
        return self.__privado_met()

encap = encapsulamiento()
print(encap.publico_atri())
encap.publico_met()