# 1. Preguntamos 10 número al operador (nos aseguramos de que son números)
#    y añadimos los números al Lista
#
# 2. Mostramos los números
#
# 3. Mostramos por pantalla la suma total de todos, la media, el cantidad de números pares 
#    y la cantidad de números impares.

#Función para insertar x items en una lista
#Parámetro array: lista donde se insertan los número
#Parámetro numItems: cantidad de número que se insertan en la lista
def AddItems(array, numItems):
    while(len(numeros) < numItems):
        num = input("Dime un número: ")
        if(num.isdigit()):
            array.append(int(num))

#Función de Calculos
#Parámetro array: lista donde se realizan los calculos
def Measures(array):
    suma = 0
    pares = 0
    impares = 0
    
    for n in array:
        print(f"Número: {n}")
        suma += n
        if(n % 2 == 0):
            pares += 1
        else:
            impares += 1
    
    print(f"Suma Total: {suma}")
    print(f"Media: {suma / len(array)}")
    print(f"Pares: {pares}")
    print(f"Impares: {impares}")

#Inicio del Programa

numeros = []

try:
    AddItems(numeros, 10)
    Measures(numeros)
except Exception as ex:
    print(f"Error: {ex}")