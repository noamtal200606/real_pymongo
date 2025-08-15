from pydantic import BaseModel

# WHY IS THE NAME OF THE FILE IN ALL CAPS
# Random space under name
# I'm pretty sure that 'id' is of type ObjectId for mongo entities. Not sure though so check it.
class student(BaseModel):
    id: constr(regex=r'^\d{9}$')
    age: int
    name: str

    grade: str
