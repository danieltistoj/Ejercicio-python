#####################################################################
# Declaración de Variables                                          #
#####################################################################
#                                                                   #
#   Sintaxis: [nombre de la varible] = [valor inicial]              #
#                                                                   #
#   Ejemplos:                                                       #
#       numero = 20                                                 #
#       saludo = "Hola a todos !!!"                                 #
#                                                                   #
#####################################################################

#Declaramos tres variables y asignamos un valor inicial
numero = 10
Numero = 20
saludo = "Hola Mundo !!!"

#Mostramos el contenido de las variables por pantalla
print(numero)
print(Numero)   #Diferencía entre mayúsculas y minúsculas
print("Saludo: " + saludo)
print("")

#Mostramos el tipo de las variables por pantalla
print(type(numero))
print(type(saludo))
print("")

#Consultamos el tipo de diferentes valores utilizando la función TYPE
print(type(3))
print(type(3.1))
print(type("3"))
print(type("pizza"))
print(type(1==1))
print(type(('1','2','3')))
print(type(["1","2","3"]))
print(type({"1","2","3"}))