from flask import Flask, app, request
from flask.templating import render_template
from models import *

#Create an index page
@app.route('/')
def indexPage():
    return render_template('index.html')

#creating login page
@app.route('/user-login')
def userLogin():
    return render_template('login.html')

#successful login
@app.route('/success-login')
def success():
    return render_template('success.html')

#creating register page
@app.route('/register/')
def registerPage():
    return render_template('register.html')

#successful register
@app.route('/success-register', methods=["POST"])
def registerSuccess():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        entry = Users(name=name,email=email,password=password)
        db.session.add(entry)
        db.session.commit()
    return render_template('login.html')


@app.route('/success-login', methods=['POST'])
def loginSucess():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        #result = db.session.query(User).all()
        result = db.session.query(Users).filter(Users.name==name, Users.password==password)
        for row in result:
            if (len(row.name)!=0):
                print("Welcome ",row.name)
                return render_template('dashboard.html', data=row.name)
    data = "Wrong Password"
    return render_template('login.html', data = data)


if __name__ == "__main__":
    app.run(debug=True, port=8000)