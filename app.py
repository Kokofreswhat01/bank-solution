from flask import Flask, render_template, request, url_for
from sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)
db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = "1306@Benie"

# ============= LES MODELS ==============

class User(db.Model, UserMixin):
     pass

@app.route("/index/")
@app.route("/index/count/")
def count():
     return render_template('HTML/count.html')

@app.route("/index/login/")
def login():
     return render_template('HTML/login.html')

@app.route("/index/register/")
def register():
     return render_template('HTML/register.html')

@app.route("/index/add_account/")
def add_count():
     return render_template('HTML/add_account.html')

@app.route("/index/withdraw/")
def withdraw():
     return render_template('HTML/withdraw.html')

@app.route("/index/information/")
def information():
     return 'Je suis l information'



if __name__=='__main__':
     app.run(debug=True)





