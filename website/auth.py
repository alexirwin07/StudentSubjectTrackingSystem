from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Student
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/', methods=['GET', 'POST'])##
def login():##
    if request.method == 'POST':
        email = request.form.get('emai')
        password = request.form.get('password')

        student = Student.query.filter_by(email=email).first()
        if student:
            if check_password_hash(student.password, password):
                flash('Logged in successfully', category='success')
                login_user(student, remember=True)
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template('Login.html')

@auth.route('/logout')##
@login_required##
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_pass = request.form.get('confirm_pass')
        surname = request.form.get('surname')
        name = request.form.get('name')

        student = Student.query.filter_by(email=email).first()
        if student:
            flash('Email already exists',category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(name) < 2:
            flash('First name must be greater than 1 characters.', category='error')
        elif password != confirm_pass:
            flash('Passwords do not match.', category='error')
        elif len(password) < 8:
            flash('Password must be at least 8 characters.', category='error')
        else:
            new_student = Student(email=email, surname=surname, name=name, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_student)
            db.session.commit()
            login_user(student, remember=True)
            flash('Account created', category='success')
            return redirect(url_for('views.home'))

    return render_template('SignUp.html')

