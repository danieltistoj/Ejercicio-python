
while(True):
    try:
        variable = float(input("Ingrese un numero: "))
        a = 2
        print("resultado: ", a * variable)
    except:
        print("Ingresaste un valor erroneo")
        print("Ingres un numero")
    else:
        print("Iniciaste sesion perfectamente")
        break
    finally:
        print("perfecto mi amigo, termino todo esto")
