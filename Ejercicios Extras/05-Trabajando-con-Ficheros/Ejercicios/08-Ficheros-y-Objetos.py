from datetime import datetime

def SearchMale(item):
    if(item.Genero == "Male"):
        return True
    else:
        return False

def SearchFemale(item):
    if(item.Genero == "Female"):
        return True
    else:
        return False

#Buscamos Clientes menones de 26 de Francia
def SearchFunc1(item):
    if(item.Edad < 26 and item.Pais == "France"):
        return True
    else:
        return False

#Buscamos Clientes Hombres de Estados Unidos
def SearchFunc2(item):
    if(item.Genero == "Male" and item.Pais == "United States"):
        return True
    else:
        return False

#Buscamos Mujeres Inglaterra mayores de 26 años
def SearchFunc3(item):
    if(item.Genero == "Female" and item.Edad > 26 and item.Pais == "Great Britain"):
        return True
    else:
        return False
        
class Cliente:
    Identificador   = None
    Nombre          = None
    Apellidos       = None
    Genero          = None
    Pais            = None
    Edad            = None
    FechaAlta       = None

    def __init__(self, id, nombre, apellidos) -> None:
        self.Identificador = id
        self.Nombre = nombre
        self.Apellidos = apellidos

################################################################################

clientes = []
path = ".\\Ficheros\\fichero.txt"
file = open(path)

for linea in (file.readlines()):
    data = linea.split(",")
    if(data[0].isdigit() == True):    
        #clientes.append(Cliente(data[7], data[1], data[2]))  
        cliente = Cliente(data[7].strip(), data[1].strip(), data[2].strip())
        cliente.Genero = data[3].strip()
        cliente.Edad = int(data[5].strip())
        cliente.Pais = data[4].strip()
        cliente.FechaAlta = datetime.strptime(data[6].strip(), "%d/%m/%Y").date()
        clientes.append(cliente)

file.close()

print(f"{len(clientes)} clientes importados.")
print("")

print(f"{len(list(filter(SearchFemale, clientes)))} clientes mujer.")
print(f"{len(list(filter(SearchMale, clientes)))} clientes hombre.")
print(f"{len(list(filter(SearchFunc1, clientes)))} clientes menores de 26 en Francia.")
print(f"{len(list(filter(SearchFunc2, clientes)))} clientes hombres en Estados Unidos.")
print(f"{len(list(filter(SearchFunc3, clientes)))} clientes mujeres mayores 26 en Inglaterra.")
print("")


print(f"{len(list(filter(lambda x: x.Genero == 'Female', clientes)))} clientes mujer.")
print(f"{len(list(filter(lambda x: x.Genero == 'Male', clientes)))} clientes hombre.")

#Buscamos Clientes menones de 26 de Francia
print(f"{len(list(filter(lambda x: x.Edad < 26 and x.Pais == 'France', clientes)))} clientes menores de 26 en Francia.")

#Buscamos Clientes Hombres de Estados Unidos
print(f"{len(list(filter(lambda x: x.Genero == 'Male' and x.Pais == 'United States', clientes)))} clientes hombres en Estados Unidos.")

#Buscamos Mujeres Inglaterra mayores de 26 años
print(f"{len(list(filter(lambda x: x.Genero == 'Female' and x.Edad > 26 and x.Pais == 'Great Britain', clientes)))} clientes mujeres mayores 26 en Inglaterra.")


#24 años / United States / Male
e = int(input("Edad: "))
p = input("Pais (France, United States, Great Britain): ")
g = input("Genero (Female o Male): ")
resultado = list(filter(lambda x: x.Edad == e and x.Pais == p and x.Genero == g, clientes))
print(f"{len(resultado)} clientes coincidentes con los criterios de búsqueda.")

contador = 0
file2 = open("resultado.txt", "wt")
file2.write("Row,First Name,Last Name,Gender,Country,Age,Date\n")

for item in resultado:
    contador += 1
    file2.write(f"{contador},{item.Nombre},{item.Apellidos},{item.Genero},{item.Pais},{item.Edad},{item.FechaAlta.strftime('%d/%m/%Y')}\n")

file2.close()