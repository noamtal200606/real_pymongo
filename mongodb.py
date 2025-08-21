from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017")
db = client["school"]

collection_of_student = db["students"]
students = list(collection_of_student.find())
