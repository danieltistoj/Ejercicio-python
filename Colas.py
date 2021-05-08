from collections import deque
colas = deque()
print(colas)

colas = deque(['Alvaro','Estudiantes','Familia','Genios'])
colas.pop()
print(colas)#saca al de la ultima posicion
#esto no funciona en las filas, solo en las colas.
colas.popleft() #saca al de la primera posicion
print(colas) 