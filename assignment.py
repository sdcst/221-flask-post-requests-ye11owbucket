from flask import Flask, request
from flask_cors import CORS
import time, json

app = Flask(__name__)  
CORS(app)      



@app.route("/json",methods=['POST'])
def jsondata():
    #url: http://127.0.0.1:5000/json
    #only POST data is allowed
    #data sent from ajax form request is retrieved 
    #response is sent back json encoded
    output = {
        "greeting" : "Hello World",
        "success" : 100,
        "timestamp" : time.time()
    }
    x = request.form
    x = dict(x)
    output['payload'] = x
    return json.dumps(output)






app.run()          
