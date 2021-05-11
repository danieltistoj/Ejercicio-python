import numpy as np
vector = np.array([6,7,1,2.3,3])
print(vector.max()) #Devuelve el mayor elemento dentro de un vector
print(vector.min()) #Devuelve el minimo elemento de un vector
print(vector.argmax()) #Devuelve la posicion del maximo valor
print(vector.argmin()) #Devuelve la posicion del valor minimo
print(vector.sum()) #Devuelve la suma de todos los elementos
print(vector.prod()) #Devuelve la multiplicacion de todos los elementos

matrizA = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("vector: ",vector)
print("Matriz: ",matrizA)
print("")
print("Vector: ",vector.size)
print("Matriz: ",matrizA.size)
