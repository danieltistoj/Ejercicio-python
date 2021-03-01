from builtins import print
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
def funcionCostoAnd(w1,w2):
                  # x0 x1 x2
    x = np.matrix([[1, 1, 1],
                   [1, 1, 0],
                   [1, 0, 1],
                   [1, 0, 0]]
                  )
    y = np.matrix([[1],
                   [0],
                   [0],
                   [0]
                   ])
    w = np.matrix([[0.5],
                   [w1],
                   [w2]
                   ])

    h = np.dot(x,w) #Realiza el producto punto
    matriztoResta = h-y
    matrizPotenciaDos = np.power(matriztoResta,2)
    suma = np.sum(matrizPotenciaDos)
    resulFinal = suma/2
    return(resulFinal)

def funcionCostoOr(w1,w2):
    # x0 x1 x2
    x = np.matrix([[1, 1, 1],
                   [1, 1, 0],
                   [1, 0, 1],
                   [1, 0, 0]]
                  )
    y = np.matrix([[1],
                   [1],
                   [1],
                   [0]
                   ])
    w = np.matrix([[0.5],
                   [w1],
                   [w2]
                   ])

    h = np.dot(x, w)  # Realiza el producto punto
    matriztoResta = h - y
    matrizPotenciaDos = np.power(matriztoResta, 2)
    suma = np.sum(matrizPotenciaDos)
    resulFinal = suma / 2
    return (resulFinal)




w1 = np.linspace(-2,2,100)
w2 = np.linspace(-2,2,100)

w1_1 ,w2_2 = np.meshgrid(w1,w2)
h = funcionCostoAnd(w1_1,w2_2) #Funcion costo para and
h2 = funcionCostoOr(w1_1,w2_2) #Funcion costo para or

#Imagen para AND
imagen = plt.figure()
subImagen = imagen.gca(projection='3d',title='Funcion costo AND')
subImagen.plot_surface(w1_1,w2_2,h,cmap=cm.coolwarm)


#imagen para OR
imagen2 = plt.figure()
subImagen2 = imagen2.gca(projection='3d',title='Funcion costo OR')
subImagen2.plot_surface(w1_1,w2_2,h2,cmap=cm.coolwarm)
plt.show()









