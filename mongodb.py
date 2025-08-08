from pymongo import MongoClient


#url = 'mongodb+srv://noamtal:<CampNou2020>@cluster0.cjce1xd.mongodb.net/'
#client = MongoClient(url)
client = MongoClient("mongodb://localhost:27017")
db = client["school"]

collection = db["students"]
students = list(collection.find())
for student in students:
    print(student)