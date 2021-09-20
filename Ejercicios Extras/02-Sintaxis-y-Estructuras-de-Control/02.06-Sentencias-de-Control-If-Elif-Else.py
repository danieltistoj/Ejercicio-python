#####################################################################
# Sentencias de Control - If / Elif / Else                          #
#####################################################################
#                                                                   #
#   Las sentencias de decisión determinar el flujo del programa     #
#   tras evaluar una expresión de comparación.                      #
#                                                                   #
#                                                                   #
#   Sintaxis:          Es igual: a == b                             #
#                   No es igual: a != b                             #
#                     Menor que: a <  b                             #
#                 Menor o igual: a <= b                             #
#                     Mayor que: a >  b                             #
#                 Mayor o igual: a >= b                             #
#                                                                   #
#####################################################################

a = 200
b = 33

#Inicio del IF
if (b > a):
  print("B es mayor que A")
elif (a == b):
  print("A y B son iguales")
else:
  print("A es mayor que B")
#Fin del IF

print("")
print("Continua el programa después del IF")