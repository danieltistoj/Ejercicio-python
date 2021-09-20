#####################################################################
# Colecciones - DICCIONARIOS                                        #
#####################################################################

# Cada valor es asociado con un clave que nos permite acceder al mismo
# No se permiten claves duplicadas
# Las claves pude ser númericas o alfanúmericas
frutasDic = {"NA":"naranja", "LI":"limón", "PO":"pomelo", "LM":"líma"}

#Utilizamos FOR para recorrer la lista de claves que nos permiten acceder a los valores
for key in frutasDic:
    print(f"Clave: {key} - Valor: {frutasDic[key]}")

#Insertar un nuevo elemento al diccionario
#Especificamos una clave nueva
frutasDic["FR"] = "Fresa"

#Modificar el valor de un elemento del diccionario
#Especificamos una clave existente
frutasDic["PO"] = "Pera"

#Eliminar un elemento del diccionario
#Especificamos una clave existente
frutasDic.pop("PO")

#Acceder al valor de un elemento del diccionario
#Especificamos una clave existente
print(frutasDic["NA"])

#Acceder al valor de un elemento del diccionario
#La función GET retorna None si no exite un elemento con la clave especificada
print(frutasDic.get("NA"))
print(frutasDic.get("SA"))