#####################################################################
# Trabajando con Ficheros - Text                                    #
#####################################################################
#                                                                   #
#   Para abrir un fichero, leer o escribir su contenido usamos      #
#   la función open() devuelve un objeto de archivo.                #
#                                                                   #
#   El objeto archivo tiene las funciones de lectura y escritura.   #
#                                                                   #
#   Sintaxis: open([ruta del fichero], [modo])                      #
#                                                                   #
#   Ejemplos:                                                       #
#       file = open("fichero.txt", "rt")                            #    
#                                                                   #
#####################################################################

# Utilizamos la función open() para abrir un fichero
# Retorna un objeto de tipo TextIOWrapper, que almacenamos en la variable fichero
fichero = open(".\\Ficheros\\fichero.txt", "rt")
print(type(fichero))

# Utilizamos la propiedad CLOSED para saber si el fichero esta abirto
print(f"Fichero Cerrado: {fichero.closed}")

# Utilizamos la función READ para leer todo el contenido
# Retorna el contenido como un alfanúmerico
contenido = fichero.read()
print(type(contenido))

# Utilizamos la función READ para leer x caractere, por ejemplo los 1000 primeros
contenido = fichero.read(1000)

# Utilizamos la función READLINE para leer linea a linea
# Retorna el contenido como un alfanúmerico
linea = fichero.readline()
print(type(linea))

# Utilizamos la función READLINES para leer todas las lineas
# Retorna el contenido como lista, cada elemento de la lista representa una línea del fichero
lineas = fichero.readlines()
print(type(lineas))

# Utilizamos FOR para leer el fichero línea a línea
# ATENCIÓN: Los siguientes for no muestran contenido, después del readlines() anterior 
# el curso se encuenta al final del fichero. Para comprobar el funcionamiento del for 
# tienes que comentar las líneas de código anteriores.
for linea in fichero:
    print(linea)

for linea in fichero.readlines():
    print(linea)

# Utilizamos la función CLOSE para cerrar el fichero
# Se recomienda cerrar el fichero para que quede bloqueado y otros programas puedan acceder
fichero.close()
print(f"Fichero Cerrado: {fichero.closed}")


