from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# make changes in flask config 
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///products.db"

# database instance
db = SQLAlchemy(app)

# Schema of database
class MyProduct(db.Model):
    # To update records in database
    productid = db.Column(db.Integer, primary_key = True)
    product = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # With repr method you can make a query from the database and print the result of query.
    # This function returns object representation in string format, used for debugging
    def __repr__(self) -> str:
        return f"{self.productid} - {self.product}"
    

# @ - Decorators in Python to tell flask what URL should trigger our function
# app.route() function returns an instance of single flask route. 
# This route can be used to handle HTTP with some optional middleware.
@app.route('/')
def hello_world():
    product=MyProduct(productid=3,product="Shoes",desc="Men Black & White Sneakers")
    db.session.add(product)
    db.session.commit()
    return render_template('index.html')
    #return "<p>Welcome to Flask</p>"

# enpoints using app.route()
@app.route('/Clothing')
def Clothing():
    return "<p>This is Clothing Page</p>"

if __name__ == "__main__":
    # change the port number 
    app.run(debug=True, port=7000)
