# import pymongo
# if __name__=="__main__":
#     print("Welcome to Pymongo")
    # coonect on local host instance same connect with remot database
    # client=pymongo.MongoClient("mongodb://localhost:27017/")
    # print(client)
    # Create database but without collection not create database also create insert method
    # Also used database
    # db=client["Lexmdb"]
    # collections=db["Lexcolcnmdb"]
    # Dictionary={"name":"Prabhash","Role":"System Engineer"}
    # collections.insert_one(Dictionary)
    # Dictionary={"name":"Akash","Role":"Test Engineer"}
    # collections.insert_one(Dictionary)
"""Insert many data"""
    # insertThese=[
    #     {"name":"Prabhash","Degination":"System Engineer","Location":"Indore","Mob":9570588189},
    #     {"name":"Akash","Degination":"Test Engineer","Location":"punjab","Mob":6204145789},
    #     {"name":"Prahlad","Degination":"NA","Location":"saharsa","Mob":8678828965},
    #     {"name":"Bhanu","Degination":"System Engineer","Location":"Indore","Mob":6202641455},
    #     {"name":"Krishna","Degination":"ShaktiKendra prmukh","Location":"Bihar","Mob":9709939919}
    # ]  
# Added underscore id set in insert
    # insertThese=[
    #     {"_id":1183163,"name":"Prabhash","Degination":"System Engineer","Location":"Indore","Mob":9570588189},
    #     {"_id":1183164,"name":"Akash","Degination":"Test Engineer","Location":"punjab","Mob":6204145789},
    #     {"_id":1183165,"name":"Prahlad","Degination":"NA","Location":"saharsa","Mob":8678828965},
    #     {"_id":1183166,"name":"Bhanu","Degination":"System Engineer","Location":"Indore","Mob":6202641455},
    #     {"_id":1183167,"name":"Krishna","Degination":"ShaktiKendra prmukh","Location":"Bihar","Mob":9709939919}
    # ]  
    # collections.insert_many(insertThese)
    # print("Successfully added")

"""Find document"""
# All modifiers use in mongo db
# random any one
# one=collections.find_one()
# for count row
# print(one.count())
# Print specific
# one=collections.find_one({"name":"Akash"})
# print(one)
# Print alldocs
# allDocs=collections.find({"name":"Akash"})
# For one fill return bydefault zero hoti hai
# allDocs=collections.find({"name":"Akash"},{"name":1,"_id":0})
# allDocs=collections.find({"name":"Akash"},{"name":0,"_id":0}).limit(1)
# print(allDocs.count())
# for item in allDocs:
#     print(item)
"""show database"""
# Showdb=client.list_database_names()
# print(Showdb)
"""Show Collections"""
# col=client['Lexmdb']
# print(col.list_collection_names())
"""Update operation"""
# if __name__=="__main__":
#     print("Welcome to Pymongo")
#     client=pymongo.MongoClient("mongodb://localhost:27017/")
#     print(client)
#     db=client["Lexmdb"]
#     collections=db["Lexcolcnmdb"]
#     prev={"Degination":"System Engineer"}
#     next={'$set':{"Location":"Rupoli"}}
    # collections.update_one(prev,next)
    # collections.update_many(prev,next)
# For modifuy count
    # up=collections.update_many(prev,next)
    # print(up.modified_count)
"""Delete Operation"""
# if __name__=="__main__":
#     print("Welcome to Pymongo")
#     client=pymongo.MongoClient("mongodb://localhost:27017/")
#     print(client)
#     db=client["Lexmdb"]
#     collections=db["Lexcolcnmdb"]
    # Delete one record
    # rec={"name":"Prahlad"}
    # # collections.delete_one(rec)
    # Delete many record
    # rec={"name":"Prabhash Kumar"}
    # up=collections.delete_many(rec)
    # print(up.deleted_count)

    
   
    