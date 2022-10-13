import time
import numpy as np

array_size = 10000

def python_version():
    t1 =time.time()
    x = range(array_size)
    y = range(array_size)
    z =[x[i] +y[i] for i in range(len(x))]
    return time.time() - t1

def numpy_version():
    t1 =time.time()
    x = np.arange(array_size)
    y = np.arange(array_size)
    z = x + y
    return time.time() - t1

t1 = python_version()
t2 = numpy_version()
print("numpy in this example :" + str(t1/t2) +  "faster")