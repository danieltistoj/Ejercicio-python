#####################################################################
# Declaración de Funciones Lambda                                   #
#####################################################################
#                                                                   #
#   Sintaxis: lambda arguments : expression                         #
#                                                                   #
#   Ejemplos:                                                       #
#       x = lambda a : a + 10                                       #
#       print(x(5))                                                 #
#                                                                   #
#####################################################################

def Saludo(nombre):
    print(f"Hola, me llamo {nombre}")

Saludo("Borja")

#La función Lambda tiene la misma funcionalidad que la función Saludo()
saluda = lambda nombre : print(f"Hola, me llamo {nombre}")
saluda("Ana")


#La función Calcular() recibe como parametro una función lambda con el calulo
#que tiene que realizar

def Multiplicar(num):
    return lambda a : a * num

def Dividir(num):
    return lambda a : a / num

def Calcular(formula):
    for n in range(1, 11, 1):  
        print(f"{n} = {formula(n)}")

Calcular(Multiplicar(25))
Calcular(Dividir(2))
Calcular(lambda a: a - 30)