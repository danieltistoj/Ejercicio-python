import numpy as np
import matplotlib.pyplot as plt

vector1 = np.random.randint(100, size=[6])
vector2 = np.random.randint(100, size=[6])
vector3 = np.random.randint(100, size=[6])


plt.plot(vector1)
plt.plot(vector2)
plt.plot(vector3)
plt.show()