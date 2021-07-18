from flask import Flask
from flask.globals import request
from flask.templating import render_template

import accepted_data

app = Flask(__name__)

@app.route("/",methods =["POST"])
def hello():
    if request.method == "POST":
        int_rate=request.form['int_rate']
        grade=request.form['grade']
        loan_status=accepted_data.loan_status_prediction(int_rate,grade)
        ls="The predicted loan status is:"+ str(loan_status) 
    else:
        ls=0
    return render_template("index.html", output = ls)


@app.route("/")
def submit():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
