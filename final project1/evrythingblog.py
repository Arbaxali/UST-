# importing Flask and other modules
from datetime import datetime
from flask import Flask
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from os import path
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.sql import func

import pymongo
import datetime
# Flask constructor


app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

db = SQLAlchemy()
DB_NAME = "database1.db"


@app.before_first_request
def create_tables():
    db.create_all() 

app.config['SECRET_KEY'] = "helloworld"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)

with app.app_context():
 db.create_all()

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())



try:
    client = pymongo.MongoClient("mongodb://localhost:27017")
    client.server_info()
    dbs = client['blogsarticles']
    db1 = client['credentialsdb']

    collection = dbs['blogsCollection']
    collection1 = db1['credsCollection']
    print(client)
    
except:
    print("cannot connect to mongodb")               




## login part
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in!", category='success')
                login_user(user, remember=True)
                return redirect("/")
            else:
                flash('Password is incorrect.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


# sign-up part

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get("email")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        email_exists = User.query.filter_by(email=email).first()
        username_exists = User.query.filter_by(username=username).first()

        if email_exists:
            flash('Email is already in use.', category='error')
        elif username_exists:
            flash('Username is already in use.', category='error')
        elif password1 != password2:
            flash('Password don\'t match!', category='error')
        elif len(username) < 2:
            flash('Username is too short.', category='error')
        elif len(password1) < 6:
            flash('Password is too short.', category='error')
        elif len(email) < 4:
            flash("Email is invalid.", category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('User created!')
            return redirect("/login")

    return render_template("signup.html", user=current_user)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/passsword-error', methods =["GET", "POST"])
def passerror():
    
    return render_template("eror.html")

@app.route('/show', methods =["GET", "POST"])
def show():
    if request.method == "POST":
        document = {
            'name': request.form.get("names"),
            'title': request.form.get("titles"),
            'article': request.form.get("textareas"),
            'last_modified': datetime.datetime.now()
        } 
        collection.insert_one(document)
        return redirect("/")   
    return render_template('show.html')

@app.route('/', methods =["GET", "POST"])
@login_required
def display():
    # if request.method == "POST":
    allproducts =collection.find({})
    return render_template('display.html', allproducts = allproducts)

if __name__=='__main__':
    app.run(host = "0.0.0.0", port=70, debug=True)









# A decorator used to tell the application
# # which URL is associated function
# @app.route('/login', methods =["GET", "POST"])
# def gfg():
#     if request.method == "POST":
#         id_name = request.form.get("idname")
#         password = request.form.get("password")
#         allproducts1 = collection1.find({})
    
#         # for item in allproducts1:
#         #     if allproducts1[item] == id_name and item.password == password:
#         #         return redirect("display")
#         #     else :
#         #         return redirect("password-error")   
#         return redirect("display") 
#     return render_template("login.html")

# @app.route('/signup', methods =["GET", "POST"])
# def signup():
#     if request.method == "POST":
#         namee = request.form.get("idna")
#         id_name = request.form.get("idname")
#         password = request.form.get("password")
#         document1 ={
#             'name': request.form.get("idna"),
#             'mailid': request.form.get("id_name"),
#             'password': request.form.get("password")
#         }
#         collection1.insert_one(document1)
#         flash('User Created!')
#         return redirect("login")
#     return render_template("signup.html")    