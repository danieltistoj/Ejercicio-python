#Variable con contenido alfanúmerico
texto = "En un lugar de la mancha de cuyo ..."

#Utilizamos la función encode() para transformar en un array de bytes
textoBytes1 = texto.encode()

#Utilizamos la función bytes() para transformar en un array de bytes
textoBytes2 = bytes(texto, "utf-8")

#Utilizamos b para asignar una variable contenido alfanúmero como un array de bytes
textoBytes3 = b"En un lugar de la mancha de cuyo ..."

#Mostramos el tipo de las variables que contienen un array de bytes
print(type(textoBytes1))
print(type(textoBytes2))
print(type(textoBytes3))

#Mostramos el contenido de un array de bytes
print(textoBytes1)
print(textoBytes2)
print(textoBytes3)

#Utilizamos la función decode() para convertir el array de bytes en contenido alfanúmerico
print(textoBytes3.decode())

#Mostramos el contenido en hexadecimal de un array de bytes
print(textoBytes1.hex())
print(textoBytes2.hex())
print(textoBytes3.hex())

#Mostramos el contenido en decimal de un array de bytes
for c in textoBytes1:
    print(c, end=" ")