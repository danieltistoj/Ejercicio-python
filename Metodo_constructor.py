# pass: Este comando es una operacion nula, no pasa nada cuando se ejecuta. Se utiliza cunado se requiere 
#por sintaxis una declaracion pero no se quiere ejecutar ningun comando o codigo.
#Se utiliza tambien en donde el codigo ira finalmente, pero no ha sido escrito finalmente
#indica que por el momento esta vacio, pero podemos tener mas atributos 
class Persona:
    pass
    def __init__(self,nombre,año):#El self es como un this en java
        self.nombre = nombre
        self.año = año
    #Los metodos siempre tienen un self
    def descripcion(self):
        #La funcion format se utiliza para ordenar el contenido de una variable
        #colocamos las llaves, donde se mostrara el contenido de la variable, respectivamente al orden en que se mandan los parametros
        return ' {} tiene {} años'.format(self.nombre,self.año)
    def comentario(self, frase):
        return '{} dice: {}'.format(self.nombre,frase)

doctor = Persona('Jose',26)
print(doctor.descripcion()) #Se imprime el nombre y edad 
print(doctor.comentario("hola que tal"))
