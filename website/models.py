from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.String(3))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    feedback = db.Column(db.String(150))
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'))

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_name = db.Column(db.String(10000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    grades = db.relationship('Grade')

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    subjects = db.relationship('Subject')
    goals = db.relationship('Goal')