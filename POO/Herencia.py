#herencia
#Clase Padre
class pokemon:
    pass
    def __init__(self,nombre,tipo):
        self.nombre = nombre
        self.tipo = tipo
    def descripcion(self):
        return 'El nombre es: {}. El tipo es: {}'.format(self.nombre,self.tipo)
#Clase hija de la clase pokemon
#Hereda atributos y metodos de la clase padre
class pikachu (pokemon):
    def ataque(self,tipo_ataque):
        return '{}, tipo de ataque: {}'.format(self.nombre,tipo_ataque)
#Clasae hija de la clase padre pokemon
class charmander(pokemon):
    def ataque(self,tipo_ataque):
        return '{}, tipo de ataque {}'.format(self.nombre,tipo_ataque)
#como pikachu es una clase hija, tambien se toman los requisitos y caracteristicas de la clase padre
nuevo_pokemon = pikachu("boby","electrico")
print(nuevo_pokemon.descripcion())
print(nuevo_pokemon.ataque("impacto trueno"))#Aqui se utiliza una funcion especifica de la clase hija 