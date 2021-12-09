from flask import Flask, app, request
from flask.templating import render_template
from models import *
import hashlib


#Create an index page
@app.route('/')
def indexPage():
    return render_template('index.html')

#creating login page
@app.route('/admin-login')
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

@app.route('/about')
def about():
    return render_template('about.html')

#successful register
@app.route('/success-register', methods=["POST"])
def registerSuccess():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        #hashing the password before storing
        hashedPassword = hashlib.md5(bytes(str(password),encoding='utf-8'))
        hashedPassword = hashedPassword.hexdigest()
        entry = Users(name=name,email=email,password=hashedPassword)
        db.session.add(entry)
        db.session.commit()
    return render_template('login.html')


@app.route('/success-login', methods=['POST'])
def loginSucess():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        #hashing the input and comparing the hash
        hashedPassword = hashlib.md5(bytes(str(password),encoding='utf-8'))
        hashedPassword = hashedPassword.hexdigest()
        if(name == "admin"):
            result = db.session.query(admin_table).filter(admin_table.name==name, admin_table.password==hashedPassword)
            for row in result:
                if (len(row.name)!=0):
                    print("Welcome ",row.name)
                    return render_template('admin_dashboard.html', data=row.name)
        result = db.session.query(Users).filter(Users.name==name, Users.password==hashedPassword)
        for row in result:
            if (len(row.name)!=0):
                print("Welcome ",row.name)
                books = db.session.query(Books).all()
                return render_template('dashboard.html', data=row.name,books=books)
    data = "Wrong Password"
    return render_template('login.html', data = data)

@app.route('/adminLoginSuccess', methods=['POST'])
def adminLoginSuccess():
    if request.method == "POST":
        title = request.form.get('title')
        category = request.form.get('category')
        author = request.form.get('author')
        entry = Books(title=title,category=category,author=author)
        db.session.add(entry)
        db.session.commit()
    return render_template('admin_dashboard.html')

@app.route('/logout')
def logout():
    return render_template('index.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')


if __name__ == "__main__":
    app.run(debug=True, port=8000)