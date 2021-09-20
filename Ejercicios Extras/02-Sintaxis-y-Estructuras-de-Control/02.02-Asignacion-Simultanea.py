#####################################################################
# Asignación Simultanea                                             #
#####################################################################
#                                                                   #
#   Sintaxis: [var1], [var2] = [var2], [var1]                       #
#                                                                   #
#   Ejemplos:                                                       #
#       a = 10                                                      #
#       b = 5                                                       #
#       a,b = b,a                                                   #
#                                                                   #
#####################################################################


#Cambie b por a. Intento 1. Forma incorrecta.
a=5
b=10
a=b
b=a
print("Intento 1. Forma incorrecta.")
print(a)
print(b)
print("")

#Cambie b por a. Intento 2. Una forma que funciona.
a=5
b=10
temp=a
a=b
b=temp
print("Intento 2. Una forma que funciona.")
print(a)
print(b)
print("")

#Cambie b por a. Intento 3. La forma de Python.
a=5
b=10
a,b = b,a
print("Intento 3. La forma de Python.")
print(a)
print(b)
print("")