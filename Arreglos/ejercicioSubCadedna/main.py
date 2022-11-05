
def resolver(cadena):
    contador = 1
    size = len(cadena)
    for x in range(0,size):
        contador_aux = 1
        for y in range(x+1,size):
            if(cadena[x]!=cadena[y]):
                #print(cadena[x]," ",cadena[y])
                contador_aux += 1
            else:
                #print(contador_aux)
                if contador < contador_aux:
                    contador = contador_aux
                break

    return contador


cadena = input("Ingrese una cadena: ")
print("Salida:",resolver(cadena))