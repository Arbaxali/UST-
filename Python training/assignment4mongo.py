import numpy as np
import pandas as pd
import pymongo
import csv


if __name__ == "__main__" :
    print("hello world")
    csvfile = open(r'C:\Users\arbazalx\OneDrive - Intel Corporation\Desktop\javasc\flames website\Flights_Delay.csv')
    reader = csv.DictReader( csvfile )
    client =pymongo.MongoClient("mongodb://localhost:27017")
    db = client['airline_delayDB']
    collection =db['flights']
    db.segment.drop()

    header = ["ID","YEAR","MONTH","DAY","DAY_OF_WEEK","AIRLINE","FLIGHT_NUMBER","TAIL_NUMBER","ORIGIN_AIRPORT","DESTINATION_AIRPORT","SCHEDULED_DEPARTURE","DEPARTURE_TIME","DEPARTURE_DELAY","TAXI_OUT","WHEELS_OFF","SCHEDULED_TIME","ELAPSED_TIME","AIR_TIME","DISTANCE","WHEELS_ON","TAXI_IN","SCHEDULED_ARRIVAL","ARRIVAL_TIME","ARRIVAL_DELAY","DIVERTED","CANCELLED","CANCELLATION_REASON","AIR_SYSTEM_DELAY",	"SECURITY_DELAY","AIRLINE_DELAY","LATE_AIRCRAFT_DELAY","WEATHER_DELAY"]

    for each in reader:
        row={}
    for field in header:
        row[field]=each[field]

    collection.insert(row)
    # def csv_to_json(filename, header=None):
    #     data = pd.read_csv(filename, header=header)
    #     return data.to_dict('records')

    # collection.insert_many(csv_to_json(r'C:\Users\arbazalx\OneDrive - Intel Corporation\Desktop\javasc\flames website\Flights_Delay.csv'))



