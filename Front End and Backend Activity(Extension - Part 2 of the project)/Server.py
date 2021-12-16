from email import message
from multiprocessing.sharedctypes import Value
from time import time
from flask import Flask, jsonify, request, render_template, jsonify
from flask_mail import Mail,Message
import pickle
import sklearn 
import pandas as pd
import random
import numpy as np
 
app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config ['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'creditcardtransac123@gmail.com'
app.config['MAIL_PASSWORD'] = 'CreditTransac@123'
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)



@app.route('/',methods=['GET','POST','DELETE'])
def getContent():
    return render_template('index.html')
 
@app.route('/process', methods=['GET','POST' ,'DELETE'])
def process():
    print("Got Data from Client:" , dict(request.get_json(force=True)))
    data = dict(request.get_json(force=True))

    with open('Credit_Fraud_Detection.pkl' , 'rb') as file:
        pickle_model = pickle.load(file)
    xTest = pd.read_csv('creditcard.csv')

    try:
        time_data = float(data['Time'].strip()) 
        amount_data = float(data['Amount'].strip())
        print(time_data)
        print(amount_data)
    except ValueError as e:
        print('Invalid Input')
        return jsonify({"message":"Invalid Input"})
    
    pca_credit = xTest[(xTest['Time']==float(data['Time'])) & (xTest['Amount']==float(data['Amount']))]
    print(pca_credit)
    if(len(pca_credit)==0):
        print('Invalid Data')
        return jsonify({"message":"INVALID DATA"})
    
    required = np.array(pca_credit)

    testData = required[0][:-1].reshape(1,-1)

    pickle_model.decision_function(testData)
    output = pickle_model.predict(testData) 
    print(output)
    msg = Message(
        'Transaction Report',
        sender = 'creditcardtransac123@gmail.com', 
        recipients= ['creditcardtransac123@gmail.com']
        )
    
    if (required[0][-1]==1.0 and output == [-1]):
        msg.body = 'It seems to be a Fraudulent Transaction'
        mail.send(msg)
        return jsonify({"message":'It seems to be a Fraudulent Transaction'})

    elif(required[0][-1]==0.0 and output == [1]):
        msg.body = 'It is a normal transaction'
        #msg.send(msg)
        return jsonify({"message":'It is a normal transaction'})
    else:
        msg.body = 'It seems to be a Fraudulent Transaction'
        mail.send(msg)
        return jsonify({"message":'It seems to be a Fraudulent Transaction'})


      
     
if __name__ == '__main__':
    app.run(debug=True,port=5555)