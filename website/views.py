from flask import Blueprint, render_template, request, flash, jsonify, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
import json
from .models import User, Subject, Grade, Goal
import sqlite3
from sqlalchemy import func, select

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('home.html', user=current_user)


@views.route("/subjects-grades", methods=["GET", "POST"])
@login_required
def alter_subjects_grades():
    possible_grades=['A*','A','B','C','D','E','F','U']
    present=False
    if request.method=="POST":               
        subject_name = request.form.get('subject')
        grade = request.form.get('grade')

        subject = Subject.query.filter_by(subject_name=subject_name, user_id=current_user.id).first()

        if bool(subject_name) and bool(grade):
            for i in range(0,len(possible_grades)):
                if grade==possible_grades[i]:
                    present=True
            if present==False:
                flash('Grade not found in algorithm. Make sure it is one of the: A*, A, B, C, D, E, F, U.', category='error')
            else:
                if subject:
                    subject_id=subject.id
                    last_grade = Grade.query.filter_by(subject_id=subject_id).order_by(Grade.date.desc())
                    try:
                        if ord(last_grade[0].grade[0]) > ord(grade[0]):
                            feedback = 'Your grades are improving, keep it up!'
                        elif ord(last_grade[0].grade[0]) < ord(grade[0]):
                            feedback = 'Your grades have dropped from your last test. Try to spend more time studying.'
                        elif ord(last_grade[0].grade[0]) == ord(grade[0]):
                            if last_grade[0].grade == 'A*' and grade == 'A':
                                feedback = 'Your grades have dropped but are still high, keep it up!'
                            elif last_grade[0].grade == 'A' and grade == 'A*':
                                feedback = 'Your grades have increased to the best, keep it up!'
                            elif grade=='A*' or grade=='A':
                                feedback = 'Your grades have stayed high from your last grade. Keep it up!'
                            elif grade=='B':
                                feedback = 'Your grades have remained at a B. This doesn\'t mean you can\' still improve. Try to spend more time revising'
                            else:
                                feedback = 'Your grades have stayed the same since your last test. Try to spend more time revising to improve this!'
                    except:
                        feedback = 'There are no grades to compare your most recent grade to. Get to logging for personalized feedback!'

                    new_grade = Grade(subject_id=subject_id, grade=grade, feedback=feedback)
                    db.session.add(new_grade)
                    db.session.commit()
                    
                    flash('Grade added.', category='success')
                else:
                    flash('Subject does not exist in database. Try just filling in the subject input box and entering before trying to add any grades', category='error')
        elif bool(subject_name):
            if subject:
                flash('Subject already in database, try adding a grade.', category='error')
            else:
                new_subject=Subject(subject_name=subject_name, user_id=current_user.id)
                db.session.add(new_subject)
                db.session.commit()
                flash('Subject successfully added.', category='success')
        elif bool(grade):
            flash('You need to enter a subject', category='error')
        else:
            flash('Type a value before entering', category='error')
    
    return render_template("grades.html", user=current_user)

@views.route("/goals", methods=["GET", "POST"])
@login_required
def goals():
    if request.method == "POST":
        
        goal = request.form.get('goal') 

        if bool(goal):

            new_goal = Goal(data=goal, user_id=current_user.id)
            db.session.add(new_goal)
            db.session.commit()
            flash('Goal added.', category='success')

        else: 
            flash('You need to enter a goal.', category='error')

    return render_template("goals.html", user=current_user)

@views.route("/delete-goal", methods = ["POST"])
def delete_goal():
    goal = json.loads(request.data)
    goalId = goal['goalId']
    goal = Goal.query.get(goalId)
    print (goal)
    if goal:
        print (goal)
        if goal.user_id == current_user.id:
            print (goal)
            db.session.delete(goal)
            db.session.commit()
    
    return jsonify({})

@views.route("/delete-grade", methods = ["POST"])
def delete_grade():
    grade = json.loads(request.data)
    gradeId = grade['gradeId']
    grade = Grade.query.get(gradeId)
    print (grade)
    if grade:
        db.session.delete(grade)
        db.session.commit()
    
    return jsonify({})

@views.route("/delete-subject", methods = ["POST"])
def delete_subject():
    subject = json.loads(request.data)
    subjectId = subject['subjectId']
    subject = Subject.query.get(subjectId)
    if subject:
        if subject.user_id == current_user.id:
            for grade in subject.grades:
                db.session.delete(grade)
            db.session.delete(subject)
            db.session.commit()
    
    return jsonify({})