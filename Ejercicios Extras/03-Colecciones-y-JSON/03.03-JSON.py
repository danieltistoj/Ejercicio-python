#####################################################################
# JSON - (JavaScript Object Notation)                               #
#####################################################################
#                                                                   #
#   Convertir de Objeto a JSON utilizamos el método json.dumps()    #
#                                                                   #
#   Convertir de JSON a Objeto utilizamos el método json.loads()    #
#                                                                   #
#####################################################################  
import json

frutas = ["naranja", "limón", "pomelo", "líma"]
frutasJSON = json.dumps(frutas)

print(type(frutas))
print(type(frutasJSON))
print(f"Fruta posición 2: {frutas[2]}")

frutas2 = json.loads(frutasJSON)
print(type(frutas2))
print(f"Fruta posición 2: {frutas2[2]}")