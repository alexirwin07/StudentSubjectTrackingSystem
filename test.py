
import render_template, request
auth=


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data=request.form
    print (data)
    return render_template("login.html", boolean=True)