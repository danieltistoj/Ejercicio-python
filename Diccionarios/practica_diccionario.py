miDiccionario = {"Alemania":"Berlín",
                 "Francia":"París",
                 "Reino Unido":"Londres",
                 "España":"Madrid"}

#como acceder a un valor concreto

print(miDiccionario["Francia"])

#Acceder aun diccionario entero

print(miDiccionario)

#Como agregar mas elementos a un diccionario

miDiccionario["Italia"] = "Lisboa"

print(miDiccionario)

#Modificar un valor a una clave

miDiccionario["Italia"] = "Roma"

print(miDiccionario)
#No pueden haber dos claves iguales
#Eliminar elementos
del miDiccionario["Reino Unido"]
print(miDiccionario)
