miDiccionario = {"Alemania":"Berlin",
                 23:"Jordan",
                 "Mosqueteros":3}
print(miDiccionario)

miTupla = ("España","Francia","Reino Unido","Alemania")
miDiccionario2 = {miTupla[0]:"Madrid",
                  miTupla[1]:"París",
                  miTupla[2]:"Londres",
                  miTupla[3]:"Berlin"
                  }
print(miDiccionario2)
print(miDiccionario2["Francia"])

miDiccionario3 = {23:"Jordan",
                  "Nombre":"Michael",
                  "Equipo":"Chicago",
                  "Anillos":(1991,1992,1993,1996,1997,1998)
                  }
print(miDiccionario3)
print(miDiccionario3["Anillos"])
#Lo siguiente muestra un diccionario con diccionario adentro que tiene adentro una tupla
miDiccionario4 = {23:"Jordan",
                  "Nombre":"Michael",
                  "Equipo":"Chicago",
                  "Anillos":{"temporadas":(1991,1992,1993,1996,1997,1998)}
                  }
#Nos devuelve las claves
print(miDiccionario4.keys())
#Imprime solo los valores
print(miDiccionario4.values())
#Mostrar el tamaño del diccionario
print(len(miDiccionario4))
