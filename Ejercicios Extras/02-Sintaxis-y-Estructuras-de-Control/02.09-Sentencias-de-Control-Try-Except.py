#####################################################################
# Sentencias de Control - Try/Except/Else/Finally                   #
#####################################################################
#                                                                   #
#   try     permite controlar las excepciones producidas en un      #
#           bloque de código.                                       #
#                                                                   #
#   except  bloque de instrucciones que se ejecutan cuando se       #
#           produce una excepción.                                  #
#                                                                   #
#   else    bloque de instrucciones que se ejecutan al finalizar    #
#           el try si no se produce un excepción.                   #
#                                                                   #
#   finally bloque de instrucciones que se ejecutan siempre que     #
#           finaliza el try, except o else.                         #
#                                                                   #
#####################################################################

numero1 = 0
numero2 = 100

try:
    numero3 = numero2 / numero1
    print(f"Número 3: {numero3}")
except ZeroDivisionError:
    print("Error ZeroDivisionError el bloque TRY")
    print("No se puede dividir entre cero.") 
except:
    print("Error en el bloque TRY")
    print("Upsss Error !!!")
else:
    print("Bloque TRY finalizado correctamente")
finally:
    print("Finalizado try o except")



###########################################################################
# Utilizamos RAISE para generar una Error controlable mediante Try/Except #
###########################################################################

numero = "32"

try:
    if(type(numero) is not int):
        raise Exception("La variable no es númerica")
except Exception as ex:
    print(ex)