from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt


app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = "1306@Benie"

@app.route("/index/")
@app.route("/index/")
def index():
     return render_template('index.html')

# ============= LES MODELS ==============

class User(db.Model, UserMixin):
     id = db.Column(db.Integer, primary_key=True)
     nom = db.Column(db.String(30),unique=True, nullable=True)
     email = db.Column(db.String(30),unique=True)
     mdp = db.Column(db.String(30),unique=True, nullable=True)

# =========================================

class RegisterForm(FlaskForm):
     nom = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "votre nom et prénom(s)"})
     
     email = EmailField(validators=[
                             InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "sylvestrebenie@gmail.com"})

     mdp = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Mot de passe"})

     inscrire = SubmitField("S'inscrire")

     def validate_username(self, nom):
        existing_user_username = User.query.filter_by(
            nom=nom.data).first()
        if existing_user_username:
            raise ValidationError(
                'Ce nom existe dejà')
class LoginForm(FlaskForm):
     nom = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "votre nom et prénom(s)"})

     password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Mot de passe"})

     submit = SubmitField('Se connecter')

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
     form = LoginForm()
     if form.validate_on_submit():
          user = User.query.filter_by(username=form.username.data).first()
          if user:
               if bcrypt.check_password_hash(user.password, form.password.data):
                    login_user(user)
                    return redirect(url_for('dashboard'))
     return render_template('login.html', form=form)

# ================================================================

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





