from sqlalchemy import Column, Integer, String
from backend.database import Base

class Students(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    password = Column(String)
    surname = Column(String)
    name = Column(String)

class Grades(Base):
    __tablename__ = "grades"

    student_id = Column(Integer, foreign_key="student_id", index=True)
    subject_id= Column(Integer, foreign_key="subject_id", index=True)
    grade= Column(String)

class Subjects(Base):
    __tablename__ ="subjects"

    student_id= Column(Integer, foreign_key="student_id", index=True)
    subject_id= Column(Integer, key=True, index=True)
    subject= Column(String)

