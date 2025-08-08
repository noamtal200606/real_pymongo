from pydantic import BaseModel


class student(BaseModel):
    id: constr(regex=r'^\d{9}$')
    age: int
    name: str
    grade: str