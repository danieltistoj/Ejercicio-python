import random

numero1 = random.randint(1, 10)
numero2 = 0

## Solución 1 ################################################################

while(numero1 != numero2):
    numero2 = int(input("Dime un número: "))
    if(numero1 != numero2):
        if (numero1 < numero2):
            print("No has acerptado, menos")
        else:
            print("No has acerptado, más") 
    else:
        print(f"Has acertado, el número es {numero1}")


## Solución 2 ################################################################

while (True):
    numero2 = int(input("Dime un número: "))
    if(numero1 != numero2):
        print("No has acerptado")
    else:
        print(f"Has acertado, el número es {numero1}")
        break   


## Solución 3 ################################################################

while(numero1 == numero1):
    numero2 = int(input("Dime un número: "))
    if(numero1 != numero2):
        print("No has acerptado")
    else:
        print(f"Has acertado, el número es {numero1}")
        break 


## Solución 4 ################################################################

while(numero1):
    numero2 = int(input("Dime un número: "))
    if(numero1 != numero2):
        print("No has acerptado")
    else:
        print(f"Has acertado, el número es {numero1}")
        break 


## Solución 5 ################################################################

acertado = False
while (acertado == False):
    numero2 = int(input("Dime un número: "))
    if(numero1 != numero2):
        print("No has acerptado")
    else:
        print(f"Has acertado, el número es {numero1}")
        acertado = True

