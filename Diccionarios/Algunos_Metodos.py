colores = {
    "Amarillo":"yellow",
    "Azul":"blue",
    "verde":"green"
}

#get()
#Busca un elemento a partir de su clave y si no lo encuentra devuelve un valor por defecto

print(colores.get('negro','no existe')) #no existe
print(colores.get('Amarillo','no existe')) #existe
#keys()
#Genera una lista en clave de los registros del diccionario
print(colores.keys())
#values()
#Genera una lista en valor de los registros del diccionario
print(colores.values())
#items()
#Genera una lista en clve-valor de los registros del diccionario
print(colores.items())

for clave,valor in colores.items():
    print(f"clave: {clave}",f"valor: {valor}")

#pop()
#Extrae un registro de un diccionario a partir de su clave y lo borra, acepta valor por defecto
print(colores.pop("Amarillo","no existe"))
print(colores.pop("negro","no existe"))
print(colores)
#clear()
#Borra todos los registros de un diccionario
colores.clear()
print(colores)