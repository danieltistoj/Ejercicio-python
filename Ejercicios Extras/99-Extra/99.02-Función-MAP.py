#####################################################################
# Función MAP                                                       #
#####################################################################
#                                                                   # 
#  La función map() transformar una colección.                      #
#                                                                   #
#  Partiendo de una coleccióin, utiliza una función que devuelve    # 
#  otra colección. La colección original no cambia                  #
#                                                                   #
#####################################################################

# Función utilizada por MAP
def Procesa(item):
    return { 'numero' : item, 'resultado' : item * 10}
    return f'{item} x 10 = {item * 10}'
    return item * n

# Colección de datos original
numeros = [52, 36, 52, 9, 125,  155, 12]

# Utilización de MAP con la función PROCESA previamente definida
print(list(map(Procesa, numeros)))

# Utilización de MAP con una función lambda
print(list(map(lambda x: x*10,numeros)))
print(list(map(lambda x: f'{x} x 10 = {x * 10}', numeros)))


    