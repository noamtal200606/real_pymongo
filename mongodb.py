from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017")
db = client["school"]

collection_of_student = db["students"]
# why use find?
students = list(collection_of_student.find())

