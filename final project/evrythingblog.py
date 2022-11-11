# from urllib import response
# from flask import Flask, render_template, request, redirect
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired 
# import requests

# app = Flask(__name__)
# app.config['SECRET_KEY'] = "hello"

# form class
# class NamerForm(FlaskForm):
#     idname = StringField("whats your name", validators=[DataRequired("name")])
#     idpass = StringField("enter pass", validators=[DataRequired("pass")])
#     Submit = SubmitField("Submit")

# @app.route('/name', methods =['GET','POST'])

# def name():
#     idname = None
#     idpass = None
#     form = NamerForm()
#     if form.validate_on_submit():
#         idname = form.idname.data
#         idpass = form.idpass.data
#         form.idname.data = ''
#         form.idpass.data = ''
#     return render_template("index1.html",idname = idname, idpass = idpass,form = form)

# importing Flask and other modules
from flask import Flask, request, render_template

# Flask constructor
app = Flask(__name__)

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
        id_name = request.form.get("fname")
        password = request.form.get("lname")
        return "Your name is "+id_name+ password
    return render_template("index1.html")

if __name__=='__main__':
    app.run(host = "0.0.0.0", port=70, debug=True)