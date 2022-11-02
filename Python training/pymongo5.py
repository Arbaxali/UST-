from xml.dom.minidom import Document
from pymongo import MongoClient
import pandas as pd
import numpy as np
import json



def mongoimport(csv_path):
    
    # drop all documents   
    hr_df = pd.read_csv(csv_path)

    payload = json.loads(hr_df.to_json(orient = 'records'))
    collection.delete_many({})
    collection.insert_many(payload)

if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017")
    print(client)
    db = client['hrdatabase1']
    collection = db['EmpCollection']
    mongoimport(r'C:\Users\arbazalx\OneDrive - Intel Corporation\Desktop\javasc\flames website\HR-Employee-Attrition.csv')

# 1 find frequency employee working in different dept

    # alldocs = collection.aggregate([
    #     {'$group' :{'_id':'$Department','totalCount' :{'$count':{}}}},
    #     {'$sort':{'total_counts': -1}},
    # ])
    # for documen in alldocs:
    #     print(documen)

# 2 top hired employees field
    alldocs2 = collection.aggregate([
        {'$group': {'_id': '$EducationField' ,'total_counts' :{'$count':{}}}},
        {'$sort':{'total_counts' :-1}},
        {'$limit':1} 
    ])        

    for docum in alldocs2:
        print(docum)

# 3 min and max

    min_maxsalary = collection.aggregate([
        {'$group' : {'_id' : 'null', 'max salary':{ '$max' : '$MonthlyIncome'},
                     'min salary' : {'$min':'$MonthlyIncome'}}}, {'$project' : {'_id' : 0}}])
    for docum in min_maxsalary:
        print(docum)

# 4. Find the AVG Monthly Income of overall employee 
    averagee =collection.aggregate([{ '$group' :
                                        {'_id' : 'null', 'averageAmount':
                                        {'$avg' : '$MonthlyIncome'}}},{'$project' : {'_id' : 0}}])
    for docu in averagee:
        print(docu)                                    
    

# 5. Find the AVG PercentSalaryHike of graduate employee employee.
    averagehike =collection.aggregate([{ '$group' :
                                        {'_id' : 'null', 'average_salary_hike':
                                        {'$avg' : '$PercentSalaryHike'}}},{'$project' : {'_id' : 0}}])
    for docu in averagehike:
        docu['average_salary_hike'] = np.round(docu['average_salary_hike'], 2)
        print(docu)                                    
                                    
    
    
# 6. Find the AVG PercentSalaryHike of employee who have left the company (Attrition = 'Yes').
    averagehikeatt = collection.aggregate([{'$match': {'Attrition':'Yes'}},
                                           { '$group' :
                                        {'_id' : 'null', 'average_salary_hike':
                                        {'$avg' : '$PercentSalaryHike'}}},{'$project' : {'_id' : 0}}

    ])
    for docu in averagehikeatt:
        docu['average_salary_hike'] = np.round(docu['average_salary_hike'], 2)
        print(docu) 
    
# 7. Highest attrition is in which department.
    deptattrition = collection.aggregate([
        {'$match':{'Attrition' :"Yes"}},
        {'$group':{'_id':'$Department','totalcounts':{'$count':{}}}}
        {'$sort': {'totalcounts':-1}}
    ])
    for item in deptattrition:
        print(item)
# 8. average salary

    emp_quali = collection.aggregate([])

