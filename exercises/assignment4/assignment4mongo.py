from xml.dom.minidom import Document
from pymongo import MongoClient
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import seaborn as sns



def mongoimport(csv_path):
    
    # drop all documents   
    hr_df = pd.read_csv(csv_path)

    payload = json.loads(hr_df.to_json(orient = 'records'))
    collection.delete_many({})
    collection.insert_many(payload)

if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017")
    print(client)
    db = client['airline_delayDB']
    collection = db['flights']
    mongoimport(r'C:\Users\arbazalx\OneDrive - Intel Corporation\Desktop\javasc\flames website\Flights_Delay.csv')


    # 1 average flight delay 

    avg_delay = collection.aggregate([
        {'$group' : {'_id' : 'null', 'avgerage_arrival_delay':{ '$avg' : '$ARRIVAL_DELAY'}}}, 
                    {'$project' : {'_id' : 0}}])
    
    for item in avg_delay:
        print(item)


   # 2 Days of months with respect to average of arrival delays. [Create a suitable plot using matplotlib/seaborn]
    # c). Days of months with respect to average of arrival delays. [Create a suitable plot using matplotlib/seaborn]
    day_avg_delay=collection.aggregate([   {'$group': {'_id':'$DAY','total_avg': { '$avg':'$ARRIVAL_DELAY'}}}  ])
    dayys = {}
    for item in day_avg_delay:
        dayys.update({item['_id']: item['total_avg']})
        
        keys1 = dayys.keys()
        values1 =dayys.values()
    plt.title("Days of month to average arrrival delay")    
    plt.bar(keys1, values1,color = 'red')
    plt.show()

    # d). Arrange weekdays with respect to the average arrival delays caused. [Create a suitable plot using matplotlib/seaborn]
    day_week=collection.aggregate([   {'$group': {'_id':'$DAY_OF_WEEK','total_avg': { '$avg':'$ARRIVAL_DELAY'}}}  ])
    daywe  = {}
    for item in day_week:
        daywe.update({item['_id'] :item['total_avg']})
    keys2 = daywe.keys()
    values2 = daywe.values()

    plt.title("weekdays to arrival delays")
    plt.bar(keys2, values2,color = 'orange')
    plt.show()

# e). Arrange Days of month as per cancellations done in descending order.  [Create a suitable plot using matplotlib/seaborn]
    day_cancel=collection.aggregate([
        {'$match':{'CANCELLED':1}},
        {'$group': {'_id': '$DAY','day_counts': { '$count':{}}}},
        {'$sort':{'DAY':-1}}])
    day_co = {}
  
    for item in day_cancel:
        day_co.update({item['_id']: item['day_counts']})
    keys3 = day_co.keys()
    values3 = day_co.values()
    plt.title("Cancellations")
    plt.bar(keys3, values3,color = 'orange')
    plt.show()

# f). Find the busiest airports with respect to day of week. Create a suitable plot using matplotlib/seaborn.
    busy_airport=collection.aggregate([
        {'$group': {'_id': '$ORIGIN_AIRPORT', 'max_day' : { '$max' : '$DAY_OF_WEEK'}}},{'$sort':{'max_day':1}},{'$limit': 20}])
    og = {}

    for item in busy_airport:
        og.update({item['_id'] :item['max_day']})

    keys4 = day_co.keys()
    values4 = day_co.values()

    plt.title("busiest airport to day of week")
    plt.bar(keys4, values4,color = 'orange')
    plt.show()

# # g). Find top 10 Airlines of US. Create a suitable plot using matplotlib/seaborn.
    top_airlines=collection.aggregate([
        {'$match':{'AIRLINE':'US'}},
        {'$group': {'_id': 'null'}},
        {'$sort':{'AIRLINE':-1}},
        {'$limit':10},{'$project':{'_id':0}}])

    for item in top_airlines:
        print(item)

# h). Finding airlines that make the maximum, minimum number of cancellations.
    min_cancellation = collection.aggregate([{'$match' : {'CANCELLED':1}},
                                   {'$group':{'_id':'$AIRLINE',
                                    'min_cancellation':{'$count':{}}}},
                                   {'$sort':{'min_cancellation': 1}}, {'$limit':1}
                                         ])
    for i in min_cancellation:
        print(i)
    
    max_cancellation = collection.aggregate([{'$match' : {'CANCELLED':1}},
                                    {'$group':{'_id':'$AIRLINE',
                                    'max_cancellation':{'$count':{}}}},
                                    {'$sort':{'max_cancellation': -1}}, {'$limit':1}
                                            ])
    for i in max_cancellation:
        print(i)


# i). Find and show airlines names in descending that make the most number of diversions made. [Create a suitable plot using matplotlib/seaborn]
    diversion=collection.aggregate([  
                                    {'$match':{'DIVERTED':1}},
                                    {'$group': {'_id':'$AIRLINE','total_counts': { '$count':{}}}},
                                    {'$sort':{'total_counts':-1}} ])
    dict = {}                                
    for item in diversion:
        dict.update({item['_id']: item['total_counts']})   
    keys = dict.keys()
    values  =dict.values()                

    plt.title("showing airline name to diversions made")
    plt.bar(keys, values)
    plt.show()

# j). Finding days of month that see the most number of diversion
    day_diversion=collection.aggregate([   {'$group': {'_id':'$AIRLINE','total_counts': { '$count':{}}}},
                                    {'$sort':{'total_counts':-1}} ])
    for item in day_diversion:
        print("day_diversion",item)       



# # k). Calculating mean and standard deviation of departure delay for all flights in minutes
    departure_delay = collection.find({},{'DEPARTURE_DELAY':1,'_id':0})
    
    departure_delay_df=pd.DataFrame(departure_delay)
    print("Mean:",departure_delay_df.mean())
    print("Standard Deviation:",departure_delay_df.std())
    
    

# L). Calculating mean and standard deviation of arrival delay for all flights in minutes
    arrival_delay = collection.find({},{'ARRIVAL_DELAY':1,'_id':0})
    
    arrival_delay_df=pd.DataFrame(arrival_delay)
    print("Mean:",arrival_delay_df.mean())
    print("Standard Deviation:",arrival_delay_df.std())



# m). Create a partitioning table ???flights_partition??? using partitioned by schema ???CANCELLED???
    no_of_diversions=collection.aggregate([{'$match':{'DIVERTED':1}},
                                    {'$group' :{'_id' : {'ORIGIN_AIRPORT':'$ORIGIN_AIRPORT',"DESTINATION_AIRPORT":'$DESTINATION_AIRPORT'},
                                               'Most_Deversions_Count':{'$sum':1}}},
                                    {'$sort':{'Most_Deversions_Count':-1}}                    ])
        
    #ii)
    no_of_diversions_df=pd.DataFrame(no_of_diversions)
    diversions_max=no_of_diversions_df.get('Most_Deversions_Count').max()
    
    print(no_of_diversions_df[no_of_diversions_df['Most_Deversions_Count']==diversions_max]['_id'])





# # o). When is the best time of day/day of week/time of a year to fly with minimum delays?

    total_delay=collection.aggregate([{'$group':{'_id':'$_id','total':{'$sum':'$ARRIVAL_DELAY'}}},{'$sort': {'total':1}},
                                  {'$limit':1}])
    for i in total_delay:
        print(i)



