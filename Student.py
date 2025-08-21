from pydantic import BaseModel, constr


class Student(BaseModel):
    id: constr(regex=r'^\d{9}$')
    age: int
    name: str
    grade: str