from flask import Flask, jsonify, request, render_template, jsonify
from flask_mail import Mail,Message 
from flask_mysqldb import MySQL
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config ['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'creditcardtransac123@gmail.com'
app.config['MAIL_PASSWORD'] = 'CreditTransac@123'
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='creditcard'
mysql = MySQL(app)
@app.route('/',methods=['GET','POST','DELETE'])
def getContent():
    return render_template('index.html')
 
@app.route('/process', methods=['GET','POST' ,'DELETE'])
def process():
    print("Got Data from Client:" , dict(request.get_json(force=True)))
    data = dict(request.get_json(force=True))

    with open('my_model.pkl' , 'rb') as file:
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
    print('required=',required)
    testData = required[0][:-1].reshape(1,-1)
    print('testData=',testData)
    pickle_model.decision_function(testData)
    output = pickle_model.predict(testData) 
    print('output=',output)
    msg = Message(
        'Transaction Report',
        sender = 'creditcardtransac123@gmail.com', 
        recipients= ['creditcardtransac123@gmail.com']
        )
    
    if ( output == [1]):
        res= 'FRAUD'
        amount = str(amount_data)
        time = str(time_data)
        #list_str = [(amount,time)]
        #result = cur.execute('SELECT Amount,Time FROM creditcard' )
        #if result>0:
            #userDetails = cur.fetchall()
        #userDetails_new = list(userDetails)
        #len_userDetails = len(userDetails_new )  
        cur = mysql.connection.cursor()  
        cur.execute("INSERT INTO creditcard(Amount,Time,Status)VALUES(%s,%s,%s)",(amount,time,res))
        msg.body = 'It seems to be a Fraudulent Transaction'
        mail.send(msg)
        return jsonify({"message":'It seems to be a Fraudulent Transaction'})

    elif( output == [0]):
        res= 'NORMAL'
        amount = str(amount_data)
        time = str(time_data)
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO creditcard(Amount,Time,Status)VALUES(%s,%s,%s)",(amount,time,res))
        msg.body = 'It is a normal transaction'
        #msg.send(msg)
        return jsonify({"message":'It is a normal transaction'})

   
     
if __name__ == '__main__':
    app.run(debug=True,port=5555)