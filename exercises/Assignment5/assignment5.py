from pymongo import MongoClient
import json


if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017")
    
    db = client['restuarantDB']
    collection = db['rescollection']
    with open(r'C:\Users\arbazalx\OneDrive - Intel Corporation\Desktop\javasc\flames website\restaurants-dataset.json',"r", encoding="utf-8") as file:
        record = file.read()
        record = record.replace('\n','')
        record = record.replace('}{','},{')
        record = "[" + record + "]"
        file_data = json.loads(record)

    if isinstance(file_data, list):
        collection.insert_many(file_data)
    else:
        collection.insert_one(file_data)        


#2.  display the fileds
    # print("*"*100)
    # cursor = collection.find({})
    # for document in cursor:
    #     print(document)
    # print("*"*100)
# 3.	Display the fields restaurant_id, name, borough, and zip code, but exclude the field _id for all the documents in the collection restaurant.
    # print("*"*100)
    # field_dis = collection.aggregate([
    #         {'$group': {'_id':{'RestuarantId':"$restaurant_id",'name':"$name", "borough": "$borough","cuisine" :"$cuisine" },
    #                     }},{'$limit': 20}])   
    # for item in field_dis:
    #     print(item)
    # print("*"*100)
# 4.Find the restaurants who achieved a score more than 90.
    # print("*"*100)
    # scores = collection.find({"grades.score":{'$gt':90}},{'_id':0,'name':1,'restaurant_id':1,'borough':1,'cuisine':1,'grades.score':1})
    # for item in scores[0:20]:
    #     print(item)
    # print("*"*100)

# 5.Show the restaurants that achieved a score, more than 80 but less than 100.
    # print("*"*100)
    # scores1 = collection.find({'$and':[{"grades.score":{'$gt':80}},{"grades.score":{'$lt':100}}]},{'_id':0,'name':1,'restaurant_id':1,'borough':1,'cuisine':1,'grades.score':1})
    # for item in scores1[0:25]:
    #     print(item)
    # print("*"*100)

# 6. Write Query to show the restaurants that do not prepare any cuisine of american & their grade score > 70.
    # print("*"*100)
    # ascendingg =collection.find({},{'_id':0,'name':1,'restaurant_id':1,'borough':1,'cuisine':1}).sort([('cuisine',1),('borough',-1)])
    # for item in ascendingg[0:50]:
    #     print(item)
    # print("*"*100)

# 7.Write a MongoDB query to arrange the name of the cuisine in an ascending order and for that same borough arranged in descending order.
    # print("*"*100)
    # descendingg=collection.find({},{'_id':0,'name':1,'restaurant_id':1,'borough':1,'cuisine':1}).sort([('cuisine',1),('borough',-1)])
    # for item in descendingg[0:50]:
    #     print(item)
    # print("*"*100)
# 8.Write a MongoDB query to arrange the name of the cuisine in descending order..
    print("*"*100)
    arrange_cusine =collection.find({},{'_id':0,'name':1,'restaurant_id':1,'cuisine':1}).sort('cuisine',-1)
    for i in arrange_cusine[0:50]:
        print(i)
    print("*"*100)    
# 9.Show the restaurant Id, name, borough and cuisines for those restaurants which prepared dish except 'American' and 'Chinese' or restaurant's name begins with letter 'Bil'.
    # print("*"*100)
    # all_documents=collection.find({'$or':[{"cuisine":{'$nin':['American ','Chinese']}},{"name":{'$regex':'^Bil'}}]},
    #                               {'_id':0,'name':1,'restaurant_id':1,'borough':1,'cuisine':1}).sort('name',1)                                                                                                                                      
    # for i in all_documents[0:50]:
    #     print(i)
    # print("*"*100)
# 10. Show the restaurant Id, name, borough and cuisines and score for restaurant's name begins with letter 'Bil'.
    # print("*"*100)                                                                                                                              
    # all_documents=collection.find({"name":{'$regex':'^Bil'}},{'_id':0,'name':1,'restaurant_id':1,'borough':1,'cuisine':1,'grades.score':1})
                                        
    # for i in all_documents[0:50]:
    #     print(i)

    # print("*"*100)
# 11.Show the restaurant Id, name, borough and cuisines and score for restaurant serving “Indian” as cuisines. 
    # print("*"*100)
    # all_documents=collection.find({"cuisine":'Indian'},
    #                               {'_id':0,'name':1,'restaurant_id':1,'borough':1,'cuisine':1,'grades.score':1})                                                                                                                                     
    # for i in all_documents[0:50]:
    #     print(i)
    # print("*"*100)
# 12.Write a MongoDB query to find the restaurant Id, name, borough, cuisines, and score for those restaurants which contain 'bi' as last three letters for its name.
    print("*"*100)
    all_documents=collection.find({"name":{'$regex':'bi$'}},
                                  {'_id':0,'name':1,'restaurant_id':1,'borough':1,'cuisine':1,'grades.score':1})
    for i in all_documents[0:50]:
        print(i)
    print("*"*100)

# 13.Write a MongoDB query to find the restaurant Id, name, borough, cuisines, and score for those restaurants which contain 'il' as last three letters for its name.
    # print("*"*100)
    # all_documents=collection.find({"name":{'$regex':'il$'}},
    #                               {'_id':0,'name':1,'restaurant_id':1,'borough':1,'cuisine':1,'grades.score':1})
    # for i in all_documents:
    #     print(i)
    # print("*"*100)
# 14.Write a query to show all the restaurant Id, name, borough, cuisines, and score for those restaurants which contain 'il' anywhere in its name.
    # print("*"*100)
    # all_documents=collection.find({"name":{'$regex':'.*il.*'}},
    #                               {'_id':0,'name':1,'restaurant_id':1,'borough':1,'cuisine':1,'grades.score':1})
    # for i in all_documents:
    #     print(i)
    # print("*"*100)    
# 15.Write a MongoDB query which will select the restaurant Id, name and grades for those restaurants which returns 0 as a remainder after dividing the score by 7.
    
    # print("*"*100)
    # all_documents=collection.find({"grades.score" :{'$mod' : [7,0]}},{"_id":0,"restaurant_id" : 1,"name":1,"grades":1})
                                                                                                                               
    # for i in all_documents:
    #     print(i)   
    # print("*"*100)    
# 16.Show document/record counts that has street and not street in addresses. 
    # print("*"*100)
    # street_in_address_count=collection.count_documents({'address.street' :{'$exists' : 1}})
    # print("Document count which contain street in address:",street_in_address_count)
    # street_not_in_address_count=collection.count_documents({'address.street' :{'$exists' : 0}})
    # print("Document count which not contain street in address:",street_not_in_address_count)
    # print("*"*100)


# 17.Write a MongoDB query to find the restaurants which do not prepare any cuisine of 'American' and achieved a score more than 70 and located in the longitude less than -65.754168 
    # print("*"*100)
    # american =collection.find({'$and':[{"cuisine":{'$ne':'American '}},{"grades.score":{'$gt':70}},{"address.coord" : {'$lt' : -65.754168}}]},
    #                               {'_id':0,'name':1,'restaurant_id':1,'borough':1,'cuisine':1,'grades.score':1})
    # for item in american:
    #     print(item)

    # print("*"*100)


