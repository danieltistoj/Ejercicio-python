def profedsor(estudiante=None):
    try:
        if estudiante is None:
            raise ValueError("Debes escribir, sino no llames a la funcion")
    except ValueError:
        print("El valor nulo no se permite")

try:
    a = float(input("Numero: "))
    10/a
except TypeError:
    print("Esto es una cadena")
except ValueError:
    print("La cadena debe de ser un numero")
except ZeroDivisionError:
    print("No se puede dividir por cero")
except Exception as x:
    print(type(x).__name__)

profedsor()