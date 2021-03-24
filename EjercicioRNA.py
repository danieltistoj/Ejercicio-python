from turtledemo.chaos import h

import matplotlib.pyplot as plt
import numpy as np
def EnergiaNeurona(p,w):
    energias = np.dot(p,w.T)#patrones por los pesos de una neurona
    energia = energias[0,0]
    return energia

def Error(t,h):
    e = t-h
    return e

def DerivadaFuncionTransicion(h):
    dh = h*(1-h)
    return dh

def Gradiante(e1,e2,h):
    gradiante = (e1+e2)*(-1)*(h-(h**2))
    return gradiante

def Wfinal(p,grad,w):
    nuevosW = np.array([])
    size = np.size(w)
    for x in range(0,size):
        print(-grad*(p[x]))
        nuevo = -grad*(p[x])+w[x]
        nuevosW = np.insert(nuevosW,x,nuevo)

    return nuevosW



def funcionTransicion(energia):
    h = 1 / (1 + np.e**(-energia))
    return h



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

nw = 0
print("capa 1")
print("Energia N1: ",EnergiaNeurona(p[0],w[0]))
hn1 = funcionTransicion(EnergiaNeurona(p[0],w[0]))
print("Hipotesis N1: ",hn1)
print("Energia N2: ",EnergiaNeurona(p[0],w[1]))
hn2 = funcionTransicion(EnergiaNeurona(p[0],w[1]))
print("Hipotesis N2: ",hn2)

nuevoPatron=np.array([])
nuevoPatron = np.insert(nuevoPatron,0,1)
nuevoPatron = np.insert(nuevoPatron,1,hn1)
nuevoPatron = np.insert(nuevoPatron,2,hn2)



print("capa 2")
#a = w.tolist()
#print(a[2])
En1=EnergiaNeurona(nuevoPatron,w[2])
print("Energia N1: ",En1)
hn1 = funcionTransicion(En1)
print("Hipotesis N1: ",hn1)
errorN1 = Error(y[0,0],hn1)
print("Error N1: ",errorN1,"\n")


En2 = EnergiaNeurona(nuevoPatron,w[3])
print("Energia N2: ",En2)
hn2 = funcionTransicion(En2)
errorN2 = Error(y[0,1],hn2)
print("Error N2: ",errorN2)
print("Hipotesis N2: ",hn2,"\n")

gradianteN1 = Gradiante(errorN1,errorN2,hn1)
gradianteN2 = Gradiante(errorN1,errorN2,hn2)

print("Gradiainte 1: ",gradianteN1)
print("Gdiante N2: ",gradianteN2,"\n")

a = w.tolist()
pesoNuevosN1 = Wfinal(nuevoPatron,gradianteN1,a[2])
print("Pesos corregidos N1 k+1: ",pesoNuevosN1)
pesoNuevosN1 = Wfinal(nuevoPatron,gradianteN2,a[3])
print("Pesos corregidos N2 k+1: ",pesoNuevosN1)







#energia, energias,row = EnergiaNeurona(p,w,nw)
#print(energias)
#print("Hipotesis: ",funcionTransicion(energia))
#print("derivada: ",DerivadaFuncionTransicion(funcionTransicion(energia)))
#h=DerivadaFuncionTransicion(funcionTransicion(energia))
#print("error: ",Error(y,h))
