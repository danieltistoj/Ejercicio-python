#####################################################################
# Trabajando con Cadenas de Texto                                   #
#####################################################################

cadena="Hola Mundo !!!"

print(cadena)
print(cadena[2])
print(cadena[2:])
print(cadena[:2])
print(cadena[2:6])
print(cadena[-2])

print(cadena.lower())
print(cadena.upper())
print(cadena.capitalize())
print(cadena.strip())
print(cadena.replace("o", "+"))
print(cadena.isdigit())

print(len(cadena))
print(cadena.count())
print("")


#####################################################################
# Formateando Cadenas y Número                                      #
#####################################################################

mensaje = "Mundo"

print("Hola " + mensaje + " !!!")
print("Hola {} !!!".format(mensaje))
print("Hola {s} !!!".format(s=mensaje))
print(f"Hola {mensaje} !!!")

numero = 10 / 3
print(numero)
print("Hola {n:1.2f} !!!".format(n=numero))