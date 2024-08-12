from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy import String, Integer, ForeignKey, Column, DateTime

class Subject(db.Model):
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'))
    subject_id = db.Column(db.String(320), primary_key=True)
    subject_name = db.Column(db.String(150))

class Student(db.Model, UserMixin):
    student_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(320), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    surname = db.Column(db.String(150))
    subjects = db.relationship('Subject')
