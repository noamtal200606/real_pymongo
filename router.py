from fastapi import APIRouter
from mongodb import collection_of_student
from Student import Student

router = APIRouter()


@router.get("/hello")
def is_alive():
    return {"msg": "Hello from router"}


@router.post("/collection_of_student")
def add_child(pupil: Student):
    collection_of_student.insert_one(pupil.dict())
    return pupil


@router.get("/collection_of_student")
def avg_students_age():
    sum_age = 0
    count = 0
    students = list(collection_of_student.find())
    for student in students:
        sum_age += int(student['age'])
        count += 1
    if count == 0:
        return {"average_age": None}
    return round(sum_age / count)


@router.put("/collection_of_student/age/{old_age}/to/{new_age}")
def update_age(new_age: int, old_age: int):
    collection_of_student.update_many(
        {'age': old_age},
        {"$set": {'age': new_age}}
    )
    students = list(collection_of_student.find())
    for student in students:
        student['_id'] = str(student['_id'])
    return students


@router.get("/collection_of_student/bigger_num/smaller_num")
def range_of_age(bigger_num: int, smaller_num: int):
    if(bigger_num > smaller_num):
        students = list(collection_of_student.find({
           'age': {
                '$gte': smaller_num,
             '$lte': bigger_num
            }
        }))
        for student in students:
            student['_id'] = str(student['_id'])
        return students
    return {'message': 'you are stupid'}


@router.delete("/collection_of_student/age")
def remove_(number: int):
    collection_of_student.delete_one({'age': int})
    students = list(collection_of_student.find())
    for student in students:
        student['_id'] = str(student['_id'])
    return students


@router.get("/collection_of_student")
def get_specific_student():
    students = list(collection_of_student.find(
        {'$and':[
        {'name': 'noam'},
        {'age': {'$gte': 25}}
        ]}))
    for student in students:
        student['_id'] = str(student['_id'])
    return students



