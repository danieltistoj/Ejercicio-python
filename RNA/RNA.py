from turtledemo.chaos import h

import matplotlib.pyplot as plt
import numpy
import numpy as np
from math import e
import pandas as pd
def EnergiaNeurona(p,w):
    energias = np.dot(p,w.T)#patrones por los pesos de una neurona
    energia = energias
    return energia

def funcionTransicion(energia):
    h = 1 / (1 + e**(-energia))
    return h

def Error(t,h):
    error = t-h
    return error

def Wfinal(p,grad,w,constante):
    nuevosW = np.array([])
    size = np.size(w)
    #print("****Tamaño:",size,w,grad,p)
    for x in range(0,size):
        nuevo = -(constante)*grad*(p[x])+w[x]
        #print("Deltas:",-(1)*grad*(p[x]))
        #print("delta:",-(0.1)*grad*(p[x]))
        nuevosW = np.insert(nuevosW,x,nuevo)
    return nuevosW

def Gradiante(sumE,h):
    gradiante = (sumE)*(-1)*(h-(h**2))
    return gradiante
def ErrorMedio(errores):
    errorMedio = 0
    for i in errores:
        errorMedio = errorMedio + (i ** 2)
    errorMedio = errorMedio / 2
    return errorMedio

def GradCapaOculta(h,pesos,g,x):
    #suma
    grad = 0
    peso = 0
    gradiante = 0
    row,col = pesos.shape

    for i in range(0,row):
        peso = pesos[i,x]
        gradiante = g[i]
        grad = grad + (peso*gradiante)
        #print("nuevo gradinte",grad)
    grad = grad * (h-(h**2))
    return grad

w1 = pd.read_csv("pesos1.csv", sep=';', comment='#').values #peso capa 1

w2 = pd.read_csv("pesos2.csv", sep=';', comment='#').values #pesos capa 2
p = pd.read_csv("patrones.csv", sep=';', comment='#').values #patron
salidas = pd.read_csv("salidas.csv", sep=';', comment='#').values #salidas de la red neurol

epoca = 2 #numero de epocas
constanteN = 1 #Es la constante de error
Emedia = np.array([]) #Array con todos los errores cuadraticos
rowp,colp = p.shape #obtenemos num patrones

#Ciclo de las epocas
for contaEpoca in range(0,epoca):
    print("*** EPOCA",contaEpoca+1,"***\n")
    ErroresEpoca = np.array([])
    #ciclo de los patrones
    for h in range(0,rowp):
        print("*** PATRON ",h+1,"***\n")
        row,col = w1.shape #obtenemos filas de pesos
        hipotesis_k0 = np.array([float(1)]) #son las salidas de la capa 0 la primera capa
        energias_k0 = np.array([])#energias de la primera capa


        #for x in range(0,rowp):
        patron_actual = p[h]
        salida_acutual = salidas[h]
        print("patron:",patron_actual)
        print("********* capa 1 **********")
        #............capa 1....................
        for i in range(0,row):
            energias_k0 = np.insert(energias_k0,i,EnergiaNeurona(patron_actual,w1[i])) #mandamos el primer patron
            hipotesis_k0 = np.insert(hipotesis_k0,i+1,funcionTransicion(energias_k0[i]))

        print("energias capa1:",energias_k0)
        print("hipotesis capa1:",hipotesis_k0)

        print("\n********* capa 2 **********")
        #............caapa 2...................

        #patron_actual = hipotesis_k0 #el patron a utilizar en la capa 2 son las hipotesis de la capa 1
        rowc2,colc2 = w2.shape #obtenemos el numero de neuronas de la capa 2, las obtenemos del numero de filas de la matriz de pesos

        hipotesis_k1 = np.array([]) #hacemos un array para las nuevas hipotesis
        energias_k1 = np.array([]) #hacemos un array para las nuevas energias
        errores = np.array([]) #hacemos un array para los errores

        for j in range(0,rowc2):
            energias_k1 = np.insert(energias_k1,j,EnergiaNeurona(hipotesis_k0,w2[j]))
            hipotesis_k1 = np.insert(hipotesis_k1,j,funcionTransicion(energias_k1[j]))
            error = Error(salida_acutual[j],funcionTransicion(energias_k1[j]))
            errores = np.insert(errores, j, error)

        print("Energias capa 2:",energias_k1)
        print("Hipotesis capa 2",hipotesis_k1)
        print("Errores:",errores)
        print("Error cuadratico:",ErrorMedio(errores))
        #Ingresamos el error cuadratico al array de la epoca
        ErroresEpoca = np.insert(ErroresEpoca,0,ErrorMedio(errores))
        #array de gradiantes de la capa 2
        gradiantes_k1 = np.array([])
        print("\n-------- Gradiantes capa 2 ---------")
        #con este ciclo obtenemos los gradiantes de la capa 2 la ultima capa y los ingresamos en un array
        for i in range(0,rowc2):
            gradiante = Gradiante(np.sum(errores),hipotesis_k1[i])
            gradiantes_k1 = np.insert(gradiantes_k1,i,gradiante)

        print("Gradiantes:",gradiantes_k1)
        print("-------- Nuevos pesos capa 2 ---------")

        nuevosPesos_k1 = np.matrix(np.empty(shape=(0,colc2), dtype=float)) #Sera la matriz con los nuevos pesos de la capa 2
        array_auxiliar = w2.tolist() #usamos este array para trabajar los pesos como vercotes y no como matrices, en lugar de que salgan de forma vertical estaran en forma horizontal
        for i in range(0,rowc2):
            nuevosPesos = Wfinal(hipotesis_k0,gradiantes_k1[i],array_auxiliar[i],constanteN)
            nuevosPesos_k1 = numpy.insert(nuevosPesos_k1, i,nuevosPesos, axis=0)
        print("Nuevos Pesos w2:",nuevosPesos_k1)

        print("\n-------- Gradiantes capa 1 ---------")
        gradiantes_k0 = np.array([])
        conta = 0;
        #recorremos los el numero de pesos que hay que nos indica el numero de neuronas
        for i in range (0,row):
            #para encotrar los gradiantes se envia a la funcion:
            #hipotesis de la neurona, los pesos de la capa 2, los grandiantes de la capa 2, y la posicion de la columna de la matriz de pesos
            #le sumamos 1 al conta porque en la posicion 0 esta x0 y tambien w0 los cuales no los necesitamos
            gradiantes_k0 = np.insert(gradiantes_k0,conta,GradCapaOculta(hipotesis_k0[conta+1],w2,gradiantes_k1,conta+1))
            conta=conta+1

        print("Gradiante:",gradiantes_k0)

        print("-------- Nuevos pesos capa 1 ---------")
        #Hacemos el mismo procedimiento para encontrar los nuevos pesos de la capa 1
        print("columnas: ",col,"filas:",row)
        print("columnas:",colc2,"filas:",rowc2)
        nuevosPesos_k0 = np.matrix(np.empty(shape=(0,col), dtype=float)) #Sera la matriz con los nuevos pesos de la capa 2
        print(w1)
        array_auxiliar = w1.tolist() #usamos este array para trabajar los pesos como vercotes y no como matrices, en lugar de que salgan de forma vertical estaran en forma horizontal
        for i in range(0,row):
            nuevosPesos = Wfinal(patron_actual,gradiantes_k0[i],array_auxiliar[i],constanteN)
            nuevosPesos_k0 = numpy.insert(nuevosPesos_k0, i,nuevosPesos, axis=0)
        print("Nuevos Pesos w1:",nuevosPesos_k0)

        #Sustituimos los nuevos pesos:
        w1 = nuevosPesos_k0
        w2 = nuevosPesos_k1
        #Fin del ciclo de una epoca
    #Este seria el fin de una epoca
    print("\nErrores cuadraticos:",ErroresEpoca)
    #Este es el error promedio por epoca
    errorPromedio = np.sum(ErroresEpoca)/rowp
    #Este error se ingresa a otro array que tiene los errores promedio por epoca
    Emedia = np.insert(Emedia,contaEpoca,errorPromedio)
#Este es el fin del ciclo de las epocas
plt.plot(Emedia)
plt.show()















