import numpy as np


x = np.zeros((10,10),dtype=int)
x[1::2,::2] = 1
x[::2,1::2] = 1
print(x)