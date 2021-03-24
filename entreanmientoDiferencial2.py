import matplotlib.pyplot as plt
import numpy as np
def obtenerDiferencial(p,w,t):
    a = np.dot(p.T, w)  # lo que obtenemos de la neurona
    if a >= 0:
        a = 1
    else:
        a = 0

    e = t - a
    diferenciaW = np.array([])

    for x in range(0,3):
        a = -2*(t-p[x]*w[x])*p[x]
        diferenciaW = np.insert(diferenciaW,x,a)


    return diferenciaW,e

dw = np.array([])
print("Patron 1")
w= np.array([0.5,-0.7,0.2]) #peso anterior
          # x1, x2, t
t=1
p1 = np.array([1,2,1]) #patron 1
print("Patron: ",p1," Pesos: ",w)
e=0

dw,e = obtenerDiferencial(p1,w,1)
print("Diferencial: ",dw)#Diferencial de pesos gradiante
print("Erorr: ",e,"\n")#Error

print("Patron 2")
p2 = np.array([1,0,-1])
print("Patron: ",p2," Pesos: ",dw)
t =1
dw,e = obtenerDiferencial(p2,dw,1)
print("Diferencial: ",dw)
print("Error: ",e,"\n")#Error

print("Patron 3")
p3 = np.array([1,-2,1])
print("Patron: ",p3," Pesos: ",dw)
t=0
dw,e = obtenerDiferencial(p2,dw,0)
print("Diferencial: ",dw)
print("Error: ",e,"\n")#Error

print("Patron 4")
p4 = np.array([1,0,2])
print("Patron: ",p4," Pesos: ",dw)
t=0
dw ,e= obtenerDiferencial(p2,w,0)
print("Diferencial: ",dw)
print("Error: ",e)#Error

x_vals = np.linspace(-5, 10, 10) # 10 valores entre 0 y 800

plt.figure(figsize=(10,8))

plt.plot(2,1, marker="o", color="red") # salida 1
plt.plot(0,-1, marker="o", color="red") # salida 0
plt.plot(-2,1, marker="o", color="blue") # slaida 0
plt.plot(0,2, marker="o", color="blue") # salida 0
plt.show()