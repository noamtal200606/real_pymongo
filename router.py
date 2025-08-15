from fastapi import APIRouter
from mongodb import collection
from STUDENT import student

router = APIRouter()

# Should be is_alive route, thats the convention to check if router is, well, alive
@router.get("/hello")
def hello():
    return {"msg": "Hello from router"}

# /collection, ummm, I have no idea what it does based on the name.
@router.post("/collection")
def add_child(pupil: student):
    collection.insert_one(pupil.dict())
    return pupil

# This can be done more efficiently, and again, route name is not indicative.
@router.get("/collection")
def avg_age():
    sum_age = 0
    count = 0
    students = list(collection.find())
    for student in students:
        if type(student['age']) == int and student['age'] != '':
            sum_age += int(student['age'])
            count += 1
    if count == 0:
        return {"average_age": None}
    return round(sum_age / count)



# Why do you have /new_number/old_number?? It's just nested routes and makes no sense.
@router.put("/collection/new_number/old_number")
def update_age(new_number: int, old_number: int):
    collection.update_many(
        {'age': old_number},
        {"$set": {'age': new_number}}
    )
    students = list(collection.find())
    for student in students:
        student['_id'] = str(student['_id'])
    return students


@router.get("/collection/bigger_num/smaller_num")
def range_of_age(bigger_num: int, smaller_num: int):
    if(bigger_num > smaller_num):
        students = list(collection.find({
           'age': {
                '$gte': smaller_num,
             '$lte': bigger_num
            }
        }))
        for student in students:
            student['_id'] = str(student['_id'])
        return students
    return {'message': 'you are stupid'}

# Again, number?? I see you remove one by age so why is the input is 'number'??
@router.delete("/collection/number")
def remove_(number: int):
    collection.delete_one({'age': number})
    students = list(collection.find())
    for student in students:
        student['_id'] = str(student['_id'])
    return students

# I have no idea what this is.
# condition what? what is the input?
@router.get("/collection")
def condition():
    students = list(collection.find(
        {'$and':[
        {'name': 'noam'},
        {'age': {'$gte': 25}}
        ]}))
    for student in students:
        student['_id'] = str(student['_id'])
    return students




