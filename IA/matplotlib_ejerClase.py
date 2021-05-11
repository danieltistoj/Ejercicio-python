from builtins import print
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


def funcionZ(x,y):
    return x*0.5+y**2+5

x = np.linspace(-2,2,100)
y = np.linspace(-2,2,100)
z = funcionZ(x,y)

#print(x)
#print(y)
#print(z)

imagen = plt.figure()
subimagen1 = imagen.add_subplot(111, projection='3d')
subimagen1.plot3D(x,y,z)
#plt.show()

x1, y1 = np.meshgrid(x,y)
z1 = funcionZ(x1,y1)

imagen2 = plt.figure()
subimagen2 = imagen2.gca(projection='3d')
subimagen2.plot_surface(x1,y1,z1, cmap = cm.coolwarm)
plt.show()
#print(z1)