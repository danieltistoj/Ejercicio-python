from turtledemo.chaos import h

import matplotlib.pyplot as plt
import numpy
import numpy as np
from math import e
def EnergiaNeurona(p,w):
    energias = np.dot(p,w.T)#patrones por los pesos de una neurona
    energia = energias[0,0]
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
    for x in range(0,size):
        nuevo = -(constante)*grad*(p[x])+w[x]
        #print("Deltas:",-(1)*grad*(p[x]))
        #print("delta:",-(0.1)*grad*(p[x]))
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


w = np.matrix([[0.5,0.8,-0.5],
                [-0.2,0.9,-0.3],
                [-0.5,-0.2,0.4],
                [0.3,0.4,0.1]]
                )

epoca = 500
constanteN = 1
Emedia = np.array([])
#Emedia2 = np.array([])
epocas = np.array([])


