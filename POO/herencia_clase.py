class Fabrica:
    def __init__(self,marca,nombre,precio,descripcion):
        self.marca = marca
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
    def __str__(self):
        return "" \
               "Marca:\t{}" \
               "\nNombre:\t{}" \
               "\nPrecio:\t{}" \
               "\nDescripcion:\t{}".format(self.marca,self.nombre,self.precio,self.descripcion)
class Auto(Fabrica):
    pass
class Deportivo(Fabrica):
    ruedas = ""
    distribucion = ""
    def __str__(self):
        return "" \
               "Marca:\t{}" \
               "\nNombre:\t{}" \
               "\nPrecio:\t{}" \
               "\nDescripcion:\t{}" \
               "\nRuedas:\t{}" \
               "\nDistribucion:\t{}".format(self.marca,self.nombre,self.precio,self.descripcion,self.ruedas,self.distribucion)

auto = Auto("ford","Ranger",100000,"camioneta")
print(auto)

deportivo = Deportivo('Volkswagen','Vento',54000,'El mejor')
deportivo.ruedas = 3
deportivo.distribucion = 'Tu autito'
print("\n",deportivo)