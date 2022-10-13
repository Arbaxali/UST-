from optparse import Values
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# fh = open(r'C:\Users\arbazalx\OneDrive - Intel Corporation\Desktop\javasc\flames website\twinkle.txt')

# fig = plt.figure(figsize= (8,6))
# plt.hist(auto_price['price'], color = 'crimson', bins= 20)
# plt.title('histogram plot auto price')
# plt.xlabel('price')
# plt.ylabel('cars')
# plt.show()


# plt.bar(range(len(dicti)), values, tick_label=names)
# plt.show()        
      
auto_price = pd.read_csv(r'C:\Users\arbazalx\OneDrive - Intel Corporation\Desktop\javasc\flames website\Automobile_price_data__Raw_.csv', sep=',')

fig = plt.figure(figsize= (30,40))
plt.style.use('seaborn-whitegrid')
plt.hist(auto_price['horsepower'], color = 'crimson', bins= 80)
plt.title('histogram plot auto price')
plt.xlabel('horsepower')
plt.ylabel('cars')
plt.show()




        

