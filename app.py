from flask import Flask, render_template, url_for, redirect
"""
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
"""

app = Flask(__name__)
# db = SQLAlchemy(app)


@app.route("/index/")
@app.route("/index/")
def index():
     return render_template('index.html')

# ============= LES MODELS ==============

# =========================================


@app.route("/index/")
@app.route("/index/count/")
def count():
     return render_template('HTML/count.html')


@app.route("/index/overview/")
def overview():
     return render_template('HTML/overview.html')

@app.route("/index/transaction/")
def transaction():
     return render_template('HTML/transaction.html')

#==================================================
@app.route("/index/login/", methods=['GET', 'POST'])
def login():
     return render_template('HTML/login.html')

# ===================================================

@app.route("/index/register/")
def register():
     return render_template('HTML/register.html')

# ================================================================

@app.route("/index/add_account/")
def add_count():
     return render_template('HTML/add_account.html')

# =================================================================

@app.route("/index/withdraw/")
def withdraw():
     return render_template('HTML/withdraw.html')

# =================================================================
@app.route("/index/information/")
def information():
     return 'Je suis l information'


if __name__=='__main__':
     app.run(debug=True)





