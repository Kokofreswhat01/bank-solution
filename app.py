from flask import Flask, render_template

app = Flask(__name__)

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

if __name__=='__main__':
     app.run(debug=True)





