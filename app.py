from flask import Flask, app, request
from flask.templating import render_template
from models import *


book_list = ['spiderman', 'spiderman', 'harry poter']
#Create an index page
@app.route('/')
def indexPage():
    return render_template('index.html')

#creating login page
@app.route('/admin-login')
@app.route('/user-login')
def userLogin():
    return render_template('login.html')

<<<<<<< HEAD

#create booklist page
@app.route('/booklist')
def booklist():
    return render_template('booklist.html', data=book_list)


#create userpanel page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', data=book_list)

#create about page
@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/success')
=======
#successful login
@app.route('/success-login')
>>>>>>> 1d5a894831c8ca3a0c1fc01998d7d6b455cf2328
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
        if(name == "admin"):
            result = db.session.query(admin_table).filter(admin_table.name==name, admin_table.password==password)
            for row in result:
                if (len(row.name)!=0):
                    print("Welcome ",row.name)
                    return render_template('admin_dashboard.html', data=row.name)
        result = db.session.query(Users).filter(Users.name==name, Users.password==password)
        for row in result:
            if (len(row.name)!=0):
                print("Welcome ",row.name)
                return render_template('dashboard.html', data=row.name)
    data = "Wrong Password"
    return render_template('login.html', data = data)


if __name__ == "__main__":
    app.run(debug=True, port=8000)