#####################################################################
# Trabajando con Ficheros - Binario                                    #
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
#       file = open("fichero.bin", "rb")                            #    
#                                                                   #
#####################################################################
import pickle
import os

texto = "En un lugar de la mancha de cuyo ..."

#Utilizamos la función write() para grabar en un fichero binario
#El contenido tiene que ser un array de bytes
file = open(".\\Ficheros\\fichero.bin", "wb")
file.write(texto.encode())
file.close()

#Utilizamos la función dump() del objeto pickle para grabar en un fichero binario
#El contenido puede ser de cualquier tipo
file = open(".\\Ficheros\\fichero.bin", "wb")
pickle.dump(texto, file)
file.close()

#Utilizamos la función load() de pickle para leer en un fichero binario
file = open(".\\Ficheros\\fichero.bin", "rb")
contenido = pickle.load(file)
print("Contenido: ", contenido)
file.close()

#Utilizamos la función remove() del objeto os para eliminar un fichero
os.remove(".\\Ficheros\\fichero.bin")



