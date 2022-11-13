# importing Flask and other modules
from flask import Flask, request, render_template ,redirect
import pymongo
import datetime
# Flask constructor
app = Flask(__name__)

try:
    client = pymongo.MongoClient("mongodb://localhost:27017")
    client.server_info()
    db = client['blogsarticles']
    collection = db['blogsCollection']
    print(client)
    
except:
    print("cannot connect to mongodb")        

# A decorator used to tell the application
# which URL is associated function
@app.route('/login', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
        id_name = request.form.get("fname")
        password = request.form.get("lname")
        return redirect("display")
    return render_template("login.html")


@app.route('/signup', methods =["GET", "POST"])
def signup():
    if request.method == "POST":
        id_name = request.form.get("fname")
        password = request.form.get("lname")
        return redirect("login")
    return render_template("signup.html")    

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
        return redirect("display")   
    return render_template('show.html')

@app.route('/display', methods =["GET", "POST"])
def display():
    # if request.method == "POST":
    allproducts =collection.find({})
    return render_template('display.html', allproducts = allproducts)

if __name__=='__main__':
    app.run(host = "0.0.0.0", port=70, debug=True)
