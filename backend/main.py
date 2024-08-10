
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    id: Optional[int]
    email: str
    password: str
    surname: str
    name: str

@app.post("/register-user")
async def register_user(student: Student):
    return student