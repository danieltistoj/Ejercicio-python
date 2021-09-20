#####################################################################
# Colecciones - LISTAS                                              #
#####################################################################

#Utilizamos [] para crear una lista
vacia  = []
frutas = ["naranja", "limón", "pomelo", "líma"]

#Mostramos todo el contenido de la lista
print(frutas)

#Mostramos el contenido de la posición 2 (pomelo)
print(frutas[2])

#Mostramos el número de veces que tenemos el valor de sandia
print(frutas.count("sandia"))

#Mostramos el número de elementos de la Lista
print(len(frutas))

#Modificamos el contenido de la posición 2 (pomelo por fresa)
frutas[2] = "fresa"

#Utilizamos APPEND para añadir nuevo elementos a la lista
frutas.append("manzana")
frutas.append("melón")

#Utilizamos POP(index) para eliminar el elemento en la posición 2
frutas.pop(2)

#Utilizamos REMOVE(value) para eliminar el elemento con valor naranja
frutas.remove("naranja")

#Comprobamos si el valor sandia existe y eliminamos
if("sandia" in frutas):
    frutas.remove("sandia")

#Utilizamos INSERT(index, value) para añadir un nuevo elemento en una posición
frutas.insert(1, "ciruela")

#Utilizamos EXTEND(values) para añadir nuevos valores a la Lista
nuevasFrutas = ["maracuya", "sandia", "kiwi", "platano"]
frutas.extend(nuevasFrutas)

#Utilizamos SORT para ordenar los elementos de la Lista
frutas.sort()
frutas.sort(reverse = True)

#Utilizamos REVERSE para invertir el orden de los elementos de la Lista
frutas.reverse()

#Utilizamos FOR para recorrer la Lista
for f in frutas:
    print(f)

#Utilizamos CLEAR para eliminar todos los elementos de la Lista
frutas.clear()