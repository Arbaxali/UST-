from itertools import count
import numpy as np
import pandas as pd


# iris_data = pd.read_csv(r'C:\Users\arbazalx\OneDrive - Intel Corporation\Desktop\javasc\flames website\iris.csv', dtype=float, usecols=[0,1,2,3])
iris_data = np.genfromtxt(r'C:\Users\arbazalx\OneDrive - Intel Corporation\Desktop\javasc\flames website\iris.csv', delimiter = ',', skip_header = 1, dtype = float, usecols=[0,1,2,3])
# print("Original array:")
# print(iris_data)
# print("Most frequent value in the above array:")
# print(np.bincount(iris_data).argmax())


# value , counts = np.unique(iris_data[:,0], return_counts = True)
# print(value[np.argmax(counts)])
# for i in iris_data:
#     print(iris_data[i].value_counts().max())

# for i in range(iris_data.shape[1]):
#     value, counts = np.unique(iris_data[: , i], return_counts= True )
#     print(value[np.argmax(counts)])
# for i in iris_data:
#     res = np.argmax([:, i] > 2.3)  
#     print(res)

# for i in range(iris_data.shape[1]):
#     print(np.argwhere(iris_data[:,:]>2.3)[0])


for i in range(iris_data.shape[1]):
    print(np.argmax(iris_data[:,i] > 2.3))    
