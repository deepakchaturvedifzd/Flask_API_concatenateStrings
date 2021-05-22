import json

from flask import Flask, request, jsonify, redirect

app = Flask(__name__)

lst=[]

@app.route('/')
def index_page():
    return "<h1> Concatenate strings</h1><br>" \
           "Input : <br><ul><li>type http://127.0.0.1:5000/tha/input/(YOUR_STRING) </li></ul><br>" \
           "Output : <br><ul><li>type http://127.0.0.1:5000/tha/output </li></ul><br>"


@app.route('/tha/input/<string:s>',methods = ['GET'])
def take_input(s):
    lst.append(s)
    return s + "==Added successfully"

@app.route('/tha/output',methods = ['GET'])
def give_output():
    out=""
    for li in lst:
        out=out+li
    return out + " !!is the concatenated string"

if __name__ == '__main__':
    app.run()
