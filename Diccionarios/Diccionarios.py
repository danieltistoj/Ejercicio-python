#Tienen una clave unica.
diccionario = {'Alvaro':'Lopez','Estudiantes':'Genios'}
type(diccionario)

print(diccionario['Alvaro'])
#Lopez
print(diccionario)
#Elimina  la clave que se referencia.
del(diccionario['Alvaro'])
print(diccionario)
edades_de_mis_estudiantes = {'estudiante':20,'otros':30}
#le suma en uno a la edad del estudiante
edades_de_mis_estudiantes['estudiante']+=1
print(edades_de_mis_estudiantes)

#imprimir un diccionario
for edades in edades_de_mis_estudiantes:
    print("nombre:",edades,"Edad:",edades_de_mis_estudiantes[edades])

lista = []
lista.append(edades_de_mis_estudiantes)
print(lista)
edades_de_mis_estudiantes={'masestudiantes':40,'masgenios':50}
lista.append(edades_de_mis_estudiantes)
print(lista)