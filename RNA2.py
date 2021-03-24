from turtledemo.chaos import h

import matplotlib.pyplot as plt
import numpy
import numpy as np
def EnergiaNeurona(p,w):
    energias = np.dot(p,w.T)#patrones por los pesos de una neurona
    energia = energias[0,0]
    return energia

def funcionTransicion(energia):
    h = 1 / (1 + np.e**(-energia))
    return h

def Error(t,h):
    e = t-h
    return e

def Wfinal(p,grad,w):
    nuevosW = np.array([])
    size = np.size(w)
    for x in range(0,size):
        #print(-grad*(p[x])," ",)
        nuevo = -grad*(p[x])+w[x]
        nuevosW = np.insert(nuevosW,x,nuevo)
    return nuevosW

def Gradiante(sumE,h):
    gradiante = (sumE)*(-1)*(h-(h**2))
    return gradiante

def GradCapaOculta(h,pesos,g,x):
    #suma
    grad = 0
    peso = 0
    gradiante = 0
    for i in range(0,2):
        peso = pesos[i,x]
        gradiante = g[i]
        grad = grad + (peso*gradiante)
    grad = grad * (h-(h**2))
    return grad

def NuevoPesos():
    return 0

p = np.matrix([[1,1,0],
              [1,0,1],
              [1,1,1],
              [1,2,0]]
              )
y = np.matrix([[1,1],
              [1,0],
              [0,0],
              [1,0]]
              )
w = np.matrix([[0.5,0.8,-0.5],
                [-0.2,0.9,-0.3],
                [-0.5,-0.2,0.4],
                [0.3,0.4,0.1]]
                )


conta1 = 0
row,col = w.shape
Emedia = np.array([])
while conta1 < 4:
    print("*** PATRON",conta1+1,"***")
    energias = np.array([])
    errores = np.array([])
    hipotesis = np.array([float(1)]) #x0 siempre va a ser 1

    capa=0
    p1 = p[conta1]
    print("Patron de entrada: ",p1)
    y2 = y.tolist()
    yActual = y2[conta1]
    print("Valores esperados: ",yActual)
    #print(yActual,yActual[0])
    i =0
    cont =0
    aux = 0 #para contar y
    while i < row:
        print("*** Capa ", capa + 1, "***")
        for x in range(i,int(row/2)):#ciclo para encontrar los pesos de una capa
            energias = np.insert(energias,x,EnergiaNeurona(p1,w[x]))
            hipotesis = np.insert(hipotesis,x+1,funcionTransicion(energias[x]))
            print("Energia N",x+1,": ",energias[x])
            print("Hipotesis N",x+1,": ",hipotesis[x+1])
            r, c = w.shape

            if r == int(row/2):
                print("y = ",yActual[aux]," h = ",funcionTransicion(energias[x]))
                error = Error(yActual[aux],funcionTransicion(energias[x]))
                errores = np.insert(errores, 0, error)
                aux = aux + 1
                print("Error: ",error)
            cont=cont+1
            print("\n")

        p1 = hipotesis #El nuevo patron de entrada para la siguiente cada sera un conjunto de las hipotesis de la capa anterior
        row = row * 2 #para que el rango quede de 2 a 4
        i = cont #para que el contador inicie en 2
        capa = capa + 1 #aunmenta a la capa siguiente
        r,c=w.shape #obtenemos las filas de la matriz de pesos
        if cont == r: #si el contador es igual al numero de filas ha terminado con las capas
            i = row

    row, col = w.shape
    gradiantes = np.array([])
    cont = 0
    x = 0
    for i in range(3,5):
        gradiante = Gradiante(np.sum(errores),p1[i])
        gradiantes = np.insert(gradiantes,x,gradiante)
        x = x +1
    #for x in range(0,int(row/2)):
    print("Energias: ",energias)
    print("Hipotesis: ",p1)
    print("Errores: ",errores)
    #print("Gradiantes: ",gradiantes)
    nuevosPesos = np.matrix(np.empty(shape=(0,3), dtype=float))
    x = 2
    j = 0
    a = w.tolist()

    for i in range(2,4):
        nw = Wfinal(p1,gradiantes[j],a[i])
        nuevosPesos = numpy.insert(nuevosPesos, j,nw, axis=0)
        #nuevosPesos=np.insert(nuevosPesos, nuevosPesos.shape[0], np.array((nw)), 0)
        #nuevosPesos = np.insert(nuevosPesos,j,nw)
        j = j +1

    #print("Pesos corregidos: ",nuevosPesos)

    gradiantes1 = gradiantes
    pesosAnt = np.matrix(np.empty(shape=(0,3), dtype=float))
    pesosAnt = np.insert(pesosAnt,0,a[2],axis=0)
    pesosAnt = np.insert(pesosAnt,1,a[3],axis=0)
    #print(pesosAnt)
    g1 = np.array([GradCapaOculta(hipotesis[1],pesosAnt,gradiantes1,1),GradCapaOculta(hipotesis[2],pesosAnt,gradiantes1,2)])
    #print(g1)
    gradiantesFinales = np.matrix(np.empty(shape=(0,2), dtype=float))
    gradiantesFinales = np.insert(gradiantesFinales,0,g1,axis=0)
    gradiantesFinales = np.insert(gradiantesFinales,1,gradiantes,axis=0)
    print("\n*** Gradiantes Finales ***")
    print(gradiantesFinales)


    p1 = p.tolist()
    p2 = p1[cont]

    for i in range(0,2):
        nw = Wfinal(p2, gradiantesFinales[0,i], a[i])
        nuevosPesos = numpy.insert(nuevosPesos, i, nw, axis=0)
        # nuevosPesos=np.insert(nuevosPesos, nuevosPesos.shape[0], np.array((nw)), 0)
        # nuevosPesos = np.insert(nuevosPesos,j,nw)
    print("\n*** Nuevos Pesos ***")
    print(nuevosPesos)

    w = nuevosPesos #Nuevos pesos
    errorMedio = 0
    #Obtener el error medio del patron
    for i in errores:
        eCuadrado = i**2
        errorMedio = errorMedio + eCuadrado
    errorMedio = errorMedio / 2
    Emedia = np.insert(Emedia,conta1,errorMedio)
    print("Errore cuadratico medio: ",Emedia)
    print("\n")
    conta1 = conta1+1

