
from pymongo import MongoClient
import pandas as pd
import json

# if __name__ == "__main__":
#     print("welcome to mongo")
#     client = MongoClient("mongodb://localhost:27017")
#     print(client)
#     db = client['pymongodb1']
#     collection = db['transactions1']

#     # alldocuments =collection.aggregate([{'$group':
#     #                                                 {'_id': '$category', 'averageAmount': {
#     #                                                     '$avg': '$amount'
#     #                                                 }}}])
#     # print(alldocuments)                                                
#     # for item in alldocuments:
#     #     print(item)

#     # allDocum = collection.aggregate([{'$group' :{'_id':'$category','totalCount' :{'$count':{}}}},{'$sort' : {'totalCount' : -1}}])   
#     # for docu in allDocum:
#     #     print(docu)
#     allDocum = collection.aggregate([{'$group' :{'_id':'$productname','totalCount' :{'$count':{}}}},{'$sort' : {'totalCount' : -1}},{'$limit': 5}])   
#     for docu in allDocum:
#         print(docu)
#     allDocum = collection.aggregate([{'$group' :{'_id':'$productname','totalCount' :{'$count':{}}}},{'$sort' : {'totalCount' : 1}},{'$limit': 5}])   
#     for docu in allDocum:
#         print(docu)

import pymongo



if __name__ == "__main__":
    print('welcome to PyMongo')
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db=client['pymongoDB']
    collection=db['transactions']

    # Run queries using pymongo on document
    all_doc=collection.aggregate([{ '$group' :
                                        {'_id' : '$category', 'averageAmount':
                                        {'$avg' : '$amount'}}}])
    for item in all_doc:
        print(item)


    # Display counts of each category in transactions
    count_category=collection.aggregate([{ '$group' :
                                        {'_id' : '$category', 'countCategory':
                                        {'$count' : {}}}}])
    # for item in count_category:
    #     print(item)
  