from flask import Flask, render_template, request, jsonify
from flask_cors import CORS,cross_origin
import numpy as np
from pickle import load

app=Flask(__name__)

@app.route('/',methods=['GET'])
@cross_origin()
def homePage():
    return render_template("try2.html")

#@app.route('/predict',methods=['GET','POST'])
#@cross_origin()
#def index():
#    try:
#        occupation=float(request.form[''])


if __name__=="__main__":
    app.run(debug=True)

