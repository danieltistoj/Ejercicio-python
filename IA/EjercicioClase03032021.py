from builtins import print
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

#funcion de w
w = np.array([ -0.7,0.2,0.5])

#funcion de patrones
patron1 = np.array([2,1,1])

t = 1 #lo que esperamos

a = np.dot(patron1,w.T) #lo que obtenemos de la neurona
print(a)
if a >= 0:
  a = 1
else:
  a = 0
print(a)

e=t-a
wnuevo=w + e*patron1
print(e)
print(wnuevo)



#p1, [1.5 1.3 1.2] = wnuevo       -   w = [0.5, -0.7, 0.2], patron1 []
#p2, [1.5 1.3 1.2] = wnuevo       -
#p3, [0.5 3.3 0.2] = wnuevo       -
#p4, [-0.5  3.3 -1.8] = wnuevo    -