from flask import Flask,request,jsonify
import random
import os

#initialize flask
app = Flask(__name__)
decision = ['yes','no']

@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg':random.choice(decision)})

if __name__ == '__main__':
    app.run(host = "0.0.0.0",)