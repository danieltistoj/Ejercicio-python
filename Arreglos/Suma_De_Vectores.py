import numpy as np
x = [1,6,2]
w = [-3,1,1]
a=0
y = []

for i in range(0,3):
    a=x[i]*w[i]
    y.append(a)

print(y)

b=0
for i in y:
    b = b+i

