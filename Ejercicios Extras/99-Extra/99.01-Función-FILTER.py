#####################################################################
# Función FILTER                                                    #
#####################################################################
#                                                                   # 
#  La función filter() busca elementos en un colección.             #
#                                                                   #
#  Utiliza una función que devuelve True cuando el elemento cumple  #
#  con los criterios de filtrado.                                   #
#                                                                   #
#####################################################################

# Utilizamos Func para buscar número mayores de 100
def Func(x):
    if(x > 100):
        return True
    else:
        return False

# Utilizamos Func2 para buscar número pares
def Func2(x):
    if(x % 2 == 0):
        return True
    else:
        return False    

numeros = [1, 85, 200, 15, 152, 450, 5, 3601, 63, 77, 8]

# Solo número mayores de 100
nums = list(filter(Func, numeros))
print(f"Mayores de 100: {nums}")

# Solo Número Pares
nums2 = list(filter(Func2, numeros))
print(f"Pares: {nums2}")

# Filtrado utilizando funciones lambda
print(f"Mayores de 100 (lambda): {list(filter(lambda x: x > 100, numeros))}")
print(f"Pares (lambda): {list(filter(lambda x: x % 2 == 0, numeros))}")