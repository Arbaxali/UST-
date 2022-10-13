from itertools import count
import numpy as np
import pandas as pd


first_series = pd.Series(list('abcdef'))


print(first_series)


np_country = np.array(['luxembourg','Norway','Japan','Switzerland','United States','Qatar','Iceland',
                       'Sweden','Singapore','Denmark'])


print(np_country)

# data_series = {    'column1' :    pd.Series([10,20,30,40] 'column2' :    pd.Series([100,200,300,400]),
# }





countries =pd.Series([7.18,7.26,7.336,7.45,7.69,7.98,8.00], index =['finalnd','denmark','danishland','enland','britain','austria','austarailia'])
print(countries)