from gc import collect
import pymongo

if __name__ == "__main__" :
    print("hello world")
    client =pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    # db = client['pymongodb']
    # collection =db['myfirstcollection']
    # all_dbs = client.list_database_names()
    # print(all_dbs)    
    collection =client['newdb']
    # print(collection.list_collection_names())
    myCollection = collection['myfirstCollection']
    print(myCollection)
    documentss = [{'_id': 4, 'name':'Lenovo Ideapad', 'price':128000, 
                  'color': ["Gray","Gold","Black"], 'ram':[4096,8196],'storage':[1024, 2048, 4096]},
                {'_id': 5, 'name':'Macbook', 'price':8000, 
                  'color': ["Black","Silver"], 'ram':[4096], 'storage': [1024, 2048]}]
    myCollection.insert_many(documentss)

    print(myCollection.distinct("name"))
    print(myCollection.distinct("price"))

    myCollection.update_one({'_id':5},{'$set':{'price':88000}})

