
from typing import Optional

from fastapi import FastAPI, Query, Path
from pydantic import BaseModel

students= {
    1: {
        "email": "alex07.irwin@btinternet.com", 
        "password": "Password01!", 
        "surname": "Irwin", 
        "name": "Alex"
    }
}

class Student(BaseModel):
    id: Optional[int] = None
    email: str
    password: str
    surname: str
    name: str

class UpdateStudent(BaseModel):
    email: Optional[str]
    password: Optional[str]
    surname: Optional[str]
    name: Optional[str]

app = FastAPI()

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="The ID of the student you want to view"), gt=0, lt=3):
    return students[student_id]

@app.post("/create-student/{student_id}")
def register_user(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}
    
    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in student:
        return{"Error": "Student does not exist"}
    
    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.year != None:
        students[student_id].year = student.year
    
    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exist"}

    del students[student_id]
    return {"Message": "Student deleted successfully"}

    

    