#####################################################################
# Sentencias de Control - For                                       #
#####################################################################
#                                                                   #
#   Sintaxis: for [variable] in [variable colección]                #
#             print([variable])                                     #
#                                                                   #
#             for [variable] in range([inicio], [fin], [intervalo]) #
#             print([variable])                                     #
#                                                                   #
#####################################################################

# Utilizamos FOR para recorrer colecciones.
# Cuando fruta es igual a pomelo se finaliza el for con break, por lo que no
# muestra el valor de lima.
citricos = ["naranja", "limón", "pomelo", "líma"]
for fruta in citricos:
  print(fruta)
  if fruta == "pomelo": 
      break

# Utilizamos FOR con RANGE para establecer un contador y ejecutar 
# sentencias repetidas veces.
# Ejemplo: de 0 a 99 de 5 en 5
for i in range(0, 100, 5):
    print(f"Número: {i}")

