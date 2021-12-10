from flask import Flask, app, request
from flask.templating import render_template
from models import *
import hashlib
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
# from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__) 
app.secret_key = 'secretkeyhardcoded'
login_manager = LoginManager()
login_manager.init_app(app)

#User auth
@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

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
        entry = Users(name=name,email=email,password=hashedPassword,book_ids="")
        db.session.add(entry)
        db.session.commit()
    return render_template('login.html')


@app.route('/success-login', methods=['POST'])
@login_required
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
                print("Welcome ",row.id)
                books = db.session.query(Books).all()
                return render_template('dashboard.html', user_id=row.id,books=books)
    data = "Wrong Password"
    return render_template('login.html', data = data)

@app.route('/adminLoginSuccess', methods=['POST'])
def adminLoginSuccess():
    if request.method == "POST":
        title = request.form.get('title')
        category = request.form.get('category')
        author = request.form.get('author')
        numberofbooks = request.form.get('numberOfBooks')
        entry = Books(title=title,category=category,author=author,numberofbooks=numberofbooks)
        db.session.add(entry)
        db.session.commit()
    return render_template('admin_dashboard.html')

@app.route('/logout')
def logout():
    return render_template('index.html')

@app.route('/admin_dashboard')
@login_required
def admin_dashboard():
    return render_template('admin_dashboard.html')

# @app.route('/dashboard/<book_id>/<user_id>')
# def dashboard(book_id,user_id):
#     result = db.session.query(Users).filter(Users.id==user_id)
#     for row in result:
#         ids = list(row.book_ids.split(" "))
#         if(book_id in ids):
#             ids.remove(book_id)
#             user_book_update = ' '.join(ids)
#             Users.query.filter_by(id=user_id).update(dict(book_ids=user_book_update))
#             db.session.commit()

#             book = Books.query.filter_by(id=book_id).first()
#             numberofbooks = book.numberofbooks
#             print("hereeeeee",numberofbooks)
#             Books.query.filter_by(id=book_id).update(dict(numberofbooks=str(int(numberofbooks)+1)))
#             db.session.commit()
#         books = db.session.query(Books).all()

#     return render_template('dashboard.html',user_id=user_id,books=books)

@app.route('/book-form-id/<book_id>/<user_id>/<numberofbooks>', methods=['GET'])
def daily_post(book_id,user_id,numberofbooks):
    #do your code here
    # print("id:",book_id)
    # print("here:", numberofbooks)
    if(int(numberofbooks)>0):
        result = db.session.query(Users).filter(Users.id==user_id)
        for row in result:
            ids = list(row.book_ids.split(" "))
            if(book_id not in ids):
                ids.append(book_id)
                Books.query.filter_by(id=book_id).update(dict(numberofbooks=str(int(numberofbooks)-1)))
                db.session.commit()
            user_book_update = ' '.join(ids)
            Users.query.filter_by(id=user_id).update(dict(book_ids=user_book_update))
            db.session.commit()
            # print('hereeeeeee',user_book_update)
    missing = Users.query.filter_by(id=user_id).first()
    user_books = list(missing.book_ids.split(" "))
    books = db.session.query(Books).all()
    for i in range(1,len(user_books)):
        user_books[i] = int(user_books[i])
    print(user_books)
    # User.query.filter(User.email.endswith('@example.com')).all()
    return render_template('issued.html',user_books=user_books,books=books,user_id=user_id)

@app.route('/issued-books')
def issued():
    
    # User.query.filter(User.email.endswith('@example.com')).all()
    return render_template('issued.html')

# @app.route('/issued-books')
# def issuedBooks():
#     books = [
#         {'id': 1, 'name':'AAA', 'author': 'Author of AAA', 'category': 'category of AAA'},
#         {'id': 2, 'name':'BBB', 'author': 'Author of BBB', 'category': 'category of BBB'},
#         {'id': 3, 'name':'CCC', 'author': 'Author of CCC', 'category': 'category of CCC'},
#         {'id': 4, 'name':'DDD', 'author': 'Author of DDD', 'category': 'category of DDD'},
#         {'id': 5, 'name':'EEE', 'author': 'Author of EEE', 'category': 'category of EEE'},

#     ]
#     return render_template('issued.html', books=books)

# # dummy routes 
# @app.route('/dashboard')
# def dashboard():
#     books = [
#         {'id': 1, 'name':'AAA', 'author': 'Author of AAA', 'category': 'category of AAA'},
#         {'id': 2, 'name':'BBB', 'author': 'Author of BBB', 'category': 'category of BBB'},
#         {'id': 3, 'name':'CCC', 'author': 'Author of CCC', 'category': 'category of CCC'},
#         {'id': 4, 'name':'DDD', 'author': 'Author of DDD', 'category': 'category of DDD'},
#         {'id': 5, 'name':'EEE', 'author': 'Author of EEE', 'category': 'category of EEE'},

#     ]
#     return render_template('dashboard.html', books=books)


if __name__ == "__main__":
    app.run(debug=True, port=8000)