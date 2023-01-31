from flask import Flask,request
from flask_cors import CORS
import json
import time
import random 

app = Flask(__name__)
CORS(app)

@app.route("/",methods=["POST","GET"])
def functo1():
    words = []
    quotes = open("dbase.txt","r")
    quotes = quotes.read()
    list = quotes.split("\n")
    for i in list:
        if i not in words:
            words.append(i)
    y = (random.choice(words))
    return y

@app.route("/admin",methods=["POST","GET"])
def functo2():
    words = []
    quotes = open('dbase.txt',"r")
    quotes = quotes.read()
    list = quotes.split("\n")
    for i in list:
        if i not in words:
            words.append(i)
        x = ''
        for i in words:
            x = x + f"{i}<br>"
        return x


@app.route("/add",methods=["POST","GET"])
def functo3():
    form_data = request.form
    form_data = dict(form_data)
    with open('dbase.txt','a') as f:
        f.write(f"\n{form_data['val1']}")
    return 'recieved'


app.run()






