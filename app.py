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
@app.route('/register')
def registerPage():
    return render_template('register.html')

#successful register
@app.route('/success-register', methods=["POST"])
def registerSuccess():
    # if request.method == "POST":
    #     name = request.form.get('name')
    #     email = request.form.get('email')
    #     password = request.form.get('password')
    #     entry = User(name=name,email=email,password=password)
    #     db.session.add(entry)
    #     db.session.commit()
    # #return render_template('success.html', form_data=data)
    return render_template('login.html')




@app.route('/loginsuccess', methods=['POST'])
def loginSucess():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        #result = db.session.query(User).all()
        result = db.session.query(User).filter(User.email==email, User.password==password)
        for row in result:
            if (len(row.email)!=0):
                print("Welcome ",row.name)
                return render_template('dashboard.html', data=row.name)
            # print("Name: ",row.name, "Email: ",row.email, "Password: ", row.password)
    data = "Wrong Password"
    return render_template('login.html', data = data)


if __name__ == "__main__":
    app.run(debug=True, port=8000)