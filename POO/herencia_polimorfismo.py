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
class Accesorios(Fabrica):
    autor=""
    fabricante=""
    def __str__(self):
        return "" \
               "Marca:\t{}" \
               "\nNombre:\t{}" \
               "\nPrecio:\t{}" \
               "\nDescripcion:\t{}" \
               "\nAutor:\t{}" \
               "\nFabricante:\t{}".format(self.marca,self.nombre,self.precio,self.descripcion,self.autor,self.fabricante)
def Descuento_Accesorio(accesorio,descuento):
    accesorio.precio = accesorio.precio - (accesorio.precio/100*descuento)
auto = Auto("ford","Ranger",100000,"camioneta")
#print(auto)
deportivo = Deportivo('Volkswagen','Vento',54000,'El mejor')
deportivo.ruedas = 3
deportivo.distribucion = 'Tu autito'
#print("\n",deportivo)

accesorio = Accesorios('Fiat','Luces de neon',10000,'Iluminan mejor')
accesorio.autor = 'Jose'
accesorio.fabricante = 'Daniel'

fabrica = [accesorio,deportivo]
fabrica.append(auto)
for x in fabrica:
    print(x,"\n")
#con isinstance se puede tratar cada subclase de forma distinta
#se puede evaluar uno por uno dependiendo de cada subclase
for x in fabrica:
    if(isinstance(x,Auto)):
        print(x.marca,x.nombre)
    elif(isinstance(x,Deportivo)):
        print(x.marca,x.nombre,x.ruedas)
    elif(isinstance(x,Accesorios)):
        print(x.marca,x.nombre,x.fabricante)

Descuento_Accesorio(accesorio,10)
print("Descuento:",accesorio.precio)
