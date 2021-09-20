numero = input("Dime un número: ")

if(numero.isdigit() == True):
    print(f"TABLA DE MULTIPLICAR DEL {numero}")
    print("========================================")
    
    for n in range(1, 11, 1):
        print(f"{n:2.0f} x {numero} = {(n * int(numero)):6.2f}")
else:
    print(f"{numero}, no es un número.")
