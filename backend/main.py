from typing import Optional

from fastapi import FastAPI, Query, Path, Depends, HTTPException, Request
from pydantic import BaseModel

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import backend.models
from backend.database import engine, SessionLocal
from sqlalchemy.orm import Session

class Student(BaseModel):
    email: str
    password: str
    surname: str
    name: str

class UpdateStudent(BaseModel):
    email: Optional[str]
    password: Optional[str]
    surname: Optional[str]
    name: Optional[str]

class Grade(BaseModel):
    subject: str
    grade: str

class UpgradeGrade(BaseModel):
    subject: Optional[str]
    grade: Optional[str]

app = FastAPI()

backend.models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally: db.close()


templates = Jinja2Templates(directory="templates")

@app.get("/get-student/{student_id}")
def get_student(db: Session = Depends(get_db)):
    return db.query(backend.models.Students).all()

@app.post("/create-student")
def register_user(student: Student, db: Session = Depends(get_db)):
    
    student_model = backend.models.Students()
    student_model.email=student.email
    student_model.password=student.password
    student_model.surname=student.surname
    student_model.name=student.name

    db.add(student_model)
    db.commit()

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent, db: Session = Depends(get_db)):


    student_model = db.query(backend.models.Students).filter(backend.models.Students.id == student_id).first()

    if student_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {student_id} : Does not exist"
        )
    
    student_model.email = student.email
    student_model.password = student.password
    student_model.surname = student.surname
    student_model.name = student.name

    db.add(student_model)
    db.commit()

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):

    student_model = db.query(backend.models.Students).filter(backend.models.Students.id == student_id).first()
    
    if student_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {student_id} : Does not exist"
        )
    
    db.query(backend.models.Students).filter(backend.models.Students.id == student_id).delete()
    
    db.commit()

@app.post("/create-grade")
def register_user(grade: Grade, db: Session = Depends(get_db)):
    
    grade_model = backend.models.Grades()
    grade_model.subject=grade.subject
    grade_model.grade=grade.grade
    grade_model.id=student.id

    db.add(student_model)
    db.commit()
    

    