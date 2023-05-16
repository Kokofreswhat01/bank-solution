from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index/")
@app.route("/index/count/")
def count():
     return render_template('count.html')


if __name__=='__main__':
     app.run(debug=True)





