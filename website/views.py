from flask import Blueprint, render_template, request, flash, jsonify, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
import json
from .models import User, Subject

views = Blueprint('views', __name__)

possible_grades=['A*','A','B','C','D','E','F','U']
grade_equiv=[9,7,6,4,3,2,1,0]

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    user_id=request.user.id
    print (user_id)
    goal = request.form.get('goal')
    subject_name = request.form.get('subject')
    grade = request.form.get('grade')

    subject = Subject.query.filter_by(subject_name=subject_name).first()

    if bool(subject_name) and bool(grade):
        print (bool(subject_name))
        for i in range(0,(len(possible_grades)-1)):
            print (i)
            if grade==possible_grades[i]:
                grade_int = grade_equiv[i]
        if grade_int==0:
            flash('Grade not found in algorithm. Make sure it is one of the: A*, A, B, C, D, E, F, U.', category='error')
        else:
            if subject:
                #add subject and grade to database
                flash('Grade added.', category='success')
            else:
                flash('Subject does not exist in database. Try just filling in the subject input box and entering before trying to add any grades', category='error')
    elif bool(subject_name):
        if subject:
            flash('Subject already in database, try adding a grade.', category='error')
        else:
            new_subject=Subject(subject_name=subject_name)
            db.session.add(new_subject)
            db.session.commit()
            flash('Subject successfully added.', category='success')
    elif bool(grade):
        flash('Try adding a subject to the database before adding a grade', category='error')
    else:
        flash('Type a value before entering', category='error')


    return render_template("home.html", user=current_user)