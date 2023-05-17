from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index/")
@app.route("/index/count/")
def count():
     return render_template('count.html')


@app.route("/index/overview/")
def overview():
     return render_template('HTML/overview.html')

@app.route("/index/transaction/")
def transaction():
     return render_template('HTML/transaction.html')


if __name__=='__main__':
     app.run(debug=True)





