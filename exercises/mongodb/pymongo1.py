from xml.dom.minidom import Document
import pymongo

if __name__ == "__main__" :
    print("hello world")
    client =pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client['pymongodb']
    collection =db['myfirstcollection']

    # Document1 ={'_id': 1, 'name':'macbook', 'price': 18000, 'color': ['red', 'green','blue'],'storage': ['64,128,256']}
    document1 = {'_id': 1, 'name':'Macbook', 'price':178000,
                  'color': ["Gray","Silver"], 'storage': [512,128,256]}

    document2 = [{'_id': 2, 'name':'lenovo', 'price':78000,'color': ["black","Silver"], 'storage': [512,1024,256]},{'_id': 3, 'name':'elitebook', 'price':278000,'color': ["Gray","red"], 'storage': [512,2048,256]}]
    # collection.insert_many(document2)
    first = collection.find_one({'_id':3})
    print(first)

    # allDocs = collection.find({})
    # for docume in allDocs:
    #     print(docume)

    allDocs = collection.find({},{'_id': 3})
    for docume in allDocs:
        print(docume)
