from encodings import utf_8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')





gold_price = pd.read_csv(r'C:\Users\arbazalx\OneDrive - Intel Corporation\Desktop\javasc\flames website\goldpriceweekly.csv')


plt.style.use('seaborn-whitegrid')
plt.figure(figsize= (13,6))
# plt.plot(gold_price['Price'], color='teal')

plt.plot(gold_price.sort_values(by= 'Price')['Price'],gold_price.sort_values(by= 'Price')['Date'])
plt.title('Price OF GOLD plot')
plt.xlabel('price')
plt.ylabel('week')
plt.show()