from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder='templates')
app.secret_key= 'my-secret-key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask_users'

mysql = MySQL(app)

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute(f"select email, password from tbl_users where email = '{email}'")
        user = cur.fetchone()
        if user and password == user[1]:
            session['email'] = user[0]
            return redirect(url_for('home'))
        else:
            return render_template(return_template='Login.html', error='Invalid username or password')
    
    return render_template("Login.html")

@app.route("/home/")
def home():
    return render_template("Home.html")

@app.route("/register/", methods=['GET','POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        surname = request.form['surname']
        name = request.form['name']

        cur = mysql.connection.cursor()
        cur.execute(f"insert into tbl_users (email, password, surname, name) values ('{email}', '{password}', '{surname}', '{name}')")
        mysql.connection.commit()
        cur.close

        return redirect(url_for('Login.html'))
    
    return render_template('SignUp.html')

@app.route("/settings/")
def settings():
    return render_template("Settings.html")

@app.route("/about-us/")
def about_us():
    return render_template("AboutUs.html")

@app.route("/progress/")
def progress():
    return render_template("Progress.html")


if __name__ == '__main__':
    app.run(debug=True)