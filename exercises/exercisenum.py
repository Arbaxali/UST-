import numpy as np
x = np.zeros((10,10))

x[1:-1,1:-1] = 1
print(x)