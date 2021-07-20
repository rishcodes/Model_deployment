from flask import Flask
from flask.globals import request
from flask.templating import render_template
import pickle
import numpy as np

model = pickle.load(open("loan.pkl", 'rb'))


app = Flask(__name__)

@app.route("/",methods =["POST"])
def hello():
    if request.method == "POST":
        loan_amnt=request.form['loan_amnt']
        annual_inc=request.form['annual_inc']
        int_rate=request.form['int_rate']
        term=request.form['term']
        grade=request.form['grade']
        
        X_test=np.array([[loan_amnt,annual_inc,int_rate,term,grade]])

        pred=model.predict(X_test)
        dict={1:"Charged Off ",
          2:"Current",
          3:"Default",
          4:"Does not meet the credit policy. Status:Charged Off",
          5:"Does not meet the credit policy. Status:Fully Paid ",
          6:"Fully Paid"}
        ls="The predicted loan status is:"+ dict[pred[0]] 
    else:
        ls=""
    return render_template("index.html", output = ls)


@app.route("/")
def submit():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
