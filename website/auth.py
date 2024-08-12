from flask import Blueprint, render_template, request, flash 

auth = Blueprint('auth', __name__)


@auth.route('/', methods=['GET', 'POST'])
def login():
    return render_template('Login.html')

@auth.route('/logout')
def logout():
    return '<p>Logout<p>'

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_pass = request.form.get('confirm_pass')
        surname = request.form.get('surname')
        name = request.form.get('name')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(name) < 2:
            flash('First name must be greater than 1 characters.', category='error')
        elif password != confirm_pass:
            flash('Passwords do not match.', category='error')
        elif len(password) < 8:
            flash('Password must be at least 8 characters.', category='error')
        else:
            flash('Account created', category='success')

    return render_template('SignUp.html')

