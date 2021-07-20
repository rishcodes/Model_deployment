import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler  
from sklearn.linear_model import LogisticRegression


def loan_status_prediction(loan_amnt,annual_inc,int_rate,term,grade):

    X_train=pd.read_csv("Logistic_X_train.csv")
    y_train=pd.read_csv("Logistic_y_train.csv")

    model=LogisticRegression()


    X_train=X_train.head(1000).iloc[:,[0,1,2,3,4]].values
    y_train=y_train.head(1000).iloc[:,[0]].values

    model.fit(X_train,y_train)
    
    print(X_train)
    print(y_train)

    X_test=np.array([[loan_amnt,annual_inc,int_rate,term,grade]])

    pred=model.predict(X_test)

    #print(model.score(X_train,y_train))

    return pred[0]

