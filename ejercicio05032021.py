from builtins import print
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from setuptools.command.alias import alias


def algoritmoEntrenamiento(w,p,t):
    a = np.dot(p.T, w)  # lo que obtenemos de la neurona
    if a >= 0:
        a = 1
    else:
        a = 0

    e = t - a
    wnuevo = w + e * p
    return wnuevo,e

def obtenerDiferencial(p,w,t):
    diferenciaW = np.array([])

    for x in range(0,3):
        a = -2*(t-p[x]*w[x])*p[x]
        diferenciaW = np.insert(diferenciaW,x,a)


    return diferenciaW


              #w1, w2, b

dw = np.array([])
print("Patron 1")
w= np.array([0.5,0.5,0.5]) #peso anterior
          # x1, x2, t
p1 = np.array([3,1,0]) #patron 1
print("Patron: ",p1," Pesos: ",w)
t=0
e=0

dw = obtenerDiferencial(p1,w,t)
print("Diferencial: ",dw)#Diferencial de pesos gradiante
print("Peso final",dw+w)
w, e = algoritmoEntrenamiento(w,p1,t)
print("Nuevos pesos: ",w)#nuevo peso
print("Erorr: ",e,"\n")#Error

print("Patron 2")
p2 = np.array([3,1,0])
print("Patron: ",p2," Pesos: ",w)
t =1
dw = obtenerDiferencial(p2,w,t)
print("Diferencial: ",dw)
print("Peso final: ",dw+w)
w,e = algoritmoEntrenamiento(w,p2,t)
print("Nuevos Pesos: ",w) #nuevo peso
print("Error: ",e,"\n")#Error

print("Patron 3")
p3 = np.array([-2,1,0])
print("Patron: ",p3," Pesos: ",w)
t=0
dw = obtenerDiferencial(p2,w,t)
print("Diferencial: ",dw)
print("Peso final: ",dw+w)
w,e=algoritmoEntrenamiento(w,p3,t)
print("Nuevo Peso: ",w)
print("Error: ",e,"\n")#Error

print("Patron 4")
p4 = np.array([2,2,0])
print("Patron: ",p4," Pesos: ",w)
t=0
dw = obtenerDiferencial(p2,w,t)
print("Diferencial: ",dw)
print("Peso final: ",dw+w)
w,e = algoritmoEntrenamiento(w,p4,t)
print("Nuevo peso: ",w)
print("Error: ",e)#Error
