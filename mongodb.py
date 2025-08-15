from pymongo import MongoClient


# Watch this: https://www.youtube.com/watch?v=Y21OR1OPC9A&ab_channel=TechWithTim
#url = 'mongodb+srv://noamtal:<CampNou2020>@cluster0.cjce1xd.mongodb.net/'
#client = MongoClient(url)
client = MongoClient("mongodb://localhost:27017")
db = client["school"]

# Again random space under for loop.
collection = db["students"]
students = list(collection.find())
for student in students:

    print(student)
