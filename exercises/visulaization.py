from enum import auto
from operator import truediv
from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


auto_price = pd.read_csv(r'C:\Users\arbazalx\OneDrive - Intel Corporation\Desktop\javasc\flames website\Automobile_price_data__Raw_.csv', sep=',')
# print(auto_price)
# print(auto_price.drop(['symboling','normalized-losses'], axis= 1, inplace= True))

cols =['bore','stroke','horsepower','peak-rpm','price']
auto_price[cols] = auto_price[cols].apply(pd.to_numeric, args =('coerce',))

# print(auto_price.isnull().sum())
# auto_price.dropna(inplace=True)
print(auto_price['price'])



# auto_price['price'].plot(kind= 'line', figsize= (15,8))
# auto_price['price'].sort_values().unique()


# plt.style.use('seaborn-whitegrid')
# plt.figure(figsize= (13,6))
# # plt.plot(auto_price['price'].sort_values().unique(), color='teal')

# plt.plot(auto_price.sort_values(by= 'price')['price'],auto_price.sort_values(by= 'price')['city-mpg'])
# plt.title('Price vs city mileage line plot')
# plt.xlabel('price')
# plt.ylabel('city mpg')
# plt.show()


## bar plot

## bivariate analysis
## bar chart used  by categorical ,nominal,vs value_counts/numerical/continous
## height of the bar represents each category

#bar plot

#used by categorical, nominal
# sns.set_style('whitegrid')
# auto_price[['price']].iloc[10:75, ].plot.bar(figsize = (15,7))

# auto_price['make'].value_counts().plot.bar(figsize = (15,7), color = 'orangered')
# plt.show()


# histogram

# fig = plt.figure(figsize= (8,6))
# plt.hist(auto_price['price'], color = 'crimson', bins= 20)
# plt.title('histogram plot auto price')
# plt.xlabel('price')
# plt.ylabel('cars')
# plt.show()

# distribution plot
# fig = plt.figure(figsize= (10,6))
# sns.distplot(auto_price['price'], bins= 20, color= 'red')
# plt.show()

# fig = plt.figure(figsize= (10,6))
# sns.distplot(auto_price['price'], bins= 20, color= 'blue', hist = True)
# plt.show()


# subplots

# plt.figure(figsize= (18,6))
# plt.subplot(1,2,1)
# plt.hist(auto_price[auto_price['num-of-doors']== 'four']['price'], bins=20)
# plt.title('histogram subplot price for four doors')
# plt.xlabel('price for four doors')
# plt.ylabel('counts of vehicle')


# plt.figure(figsize= (18,6))
# plt.subplot(1,2,2)
# plt.hist(auto_price[auto_price['num-of-doors']== 'two']['price'], bins=20 ,color= "green")
# plt.title('histogram subplot price for four doors')
# plt.xlabel('price for(two doors')
# plt.ylabel('counts of vehicle')
# plt.show()

# scatter plot

# alpha = transperancy
# marker = changing scatter plot style [o,x,X,s,d,>,<,*,.,^]

# plt.figure(figsize=(10,7))
# sns.scatterplot(x = auto_price['city-mpg'], y= auto_price['price'], color ='orangered', marker = 's', alpha =0.7)
# plt.show()

# plt.figure(figsize= (6,6))
# plt.subplot(1,2,1)
# sns.scatterplot(x = auto_price['highway-mpg'],y = auto_price[auto_price['body-style'] == 'convertible']['price'], color = 'orange',markers= 's',alpha =0.8)
# plt.title('scatter subplot for convertibles')
# plt.xlabel('highway mileage')
# plt.ylabel('Convertible body style')
# plt.show()

# plt.figure(figsize= (6,6))
# plt.subplot(1,2,2)
# sns.scatterplot(x = auto_price['highway-mpg'],y = auto_price[auto_price['body-style'] == 'sedan']['price'], color = 'orange',markers= 's',alpha =0.8)
# plt.title('scatter subplot for convertibles')
# plt.xlabel('highway mileage')
# plt.ylabel('sedan body style')
# plt.show()

# plt.figure(figsize= (6,6))
# plt.subplot(1,2,3)
# sns.scatterplot(x = auto_price['highway-mpg'],y = auto_price[auto_price['body-style'] == 'hatchback']['price'], color = 'orange',markers= 's',alpha =0.8)
# plt.title('scatter subplot for convertibles')
# plt.xlabel('highway mileage')
# plt.ylabel('hatchback body style')
# plt.show()

# plt.figure(figsize= (6,6))
# plt.subplot(1,2,3)
# sns.scatterplot(x = auto_price['highway-mpg'],y = auto_price[auto_price['body-style'] == 'wagon']['price'], color = 'orange',markers= 's',alpha =0.8)
# plt.title('scatter subplot for convertibles')
# plt.xlabel('highway mileage')
# plt.ylabel('wagon body style')
# plt.show()

# plt.figure(figsize= (6,6))
# plt.subplot(1,2,4)
# sns.scatterplot(x = auto_price['highway-mpg'],y = auto_price[auto_price['body-style'] == 'hardtop']['price'], color = 'orange',markers= 's',alpha =0.8)
# plt.title('scatter subplot for convertibles')
# plt.xlabel('highway mileage')
# plt.ylabel(' bodyhardtop style')
# plt.show()


# body_style = list(auto_price['body-style'].unique())


# for index, style in enumerate(body_style):
#     fig.add_subplot(3,2, index + 1)
#     sns.scatterplot(x = auto_price[auto_price['body-style']== 'style']['highway-mpg'], y = auto_price[auto_price['body-style'] == 'style']['price'], color = 'orange',markers= 's',alpha =0.8)

# plt.show()

# plt.figure(figsize = (18,13))
# for index, style in enumerate(body_style):
#     plt.subplot(2, 3, index + 1)
#     sns.scatterplot(x = auto_price[auto_price['body-style'] == style]['city-mpg'], 
#             y = auto_price[auto_price['body-style'] == style]['price'], color = 'orangered', marker='s')
# plt.show()



# Display Density Plot 
fig = plt.figure(figsize = (10,6))
sns.distplot(auto_price['highway-mpg'], bins = 20, color = 'b', hist = False)
plt.axvline(auto_price['highway-mpg'].mean(), linestyle = '--', color = 'k')
plt.axvline(auto_price['highway-mpg'].median(), linestyle = '--', color = 'red')
plt.show()

