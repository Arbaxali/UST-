import numpy as np
iris_data
iris_data[(iris_data[:,:] == 3.4) | (iris_data[:,:] == 1.7)] = np.nan
np.isnan(iris_data).sum(axis =0)