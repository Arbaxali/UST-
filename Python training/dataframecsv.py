from enum import auto
import numpy as np
import pandas as pd


auto_price = pd.read_csv(r'C:\Users\arbazalx\OneDrive - Intel Corporation\Desktop\javasc\flames website\Automobile_price_data__Raw_.csv')
print(auto_price)     

# print(auto_price.head())  #print head

print(auto_price.tail())  # print tail last 5 
print(auto_price.shape)
print(auto_price.columns)



print(auto_price.replace('?', np.nan))
print(auto_price.isnull().sum())



# reverse all  columns

print(auto_price.iloc[10:20, ::-1])

df_rand = auto_price.sample(frac=0.2)
print(df_rand)

print(auto_price.query("make == 'toyota' and `engine-size` > 100 and `drive-wheels` == 'fwd' "))

print(auto_price.groupby(['make'])[['city-mpg','highway-mpg']].mean().sort_values(by = 'city-mpg'))


data_series1 = pd.Series([10,20,30,40,50,60, 70])
data_series2 = pd.Series([20,40,60,80,100,120,140,160])

