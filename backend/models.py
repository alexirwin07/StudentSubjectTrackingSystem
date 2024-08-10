from sqlalchemy import Column, Integer, String
from backend.database import Base

class Students(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    password = Column(String)
    surname = Column(String)
    name = Column(String)

class Grades(Base):
    __tablename__ = "grades"

    grade_id= Column(Integer, primary_key=True, index=True)
    id = Column(Integer, foreign_key=True, index=True)
    subject= Column(String)
    grade= Column(String)

