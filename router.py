from fastapi import APIRouter
from mongodb import collection
from STUDENT import student

router = APIRouter()


@router.get("/hello")
def hello():
    return {"msg": "Hello from router"}


@router.post("/collection")
def add_child(pupil: student):
    collection.insert_one(pupil.dict())
    return pupil


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

@router.delete("/collection/number")
def remove_(number: int):
    collection.delete_one({'age': number})
    students = list(collection.find())
    for student in students:
        student['_id'] = str(student['_id'])
    return students


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



