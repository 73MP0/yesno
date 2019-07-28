from flask import Flask,request,jsonify
import random
import os

#initialize flask
app = Flask(__name__)
decision = ['yes','no']

#create get method
@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg':random.choice(decision)})

#locally host on port 80
if __name__ == '__main__':
    app.run(host = "0.0.0.0", port=80)