from flask import Flask, render_template, request, jsonify
from flask_cors import CORS,cross_origin
import numpy as np
from pickle import load

app=Flask(__name__)

@app.route('/',methods=['GET'])
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['GET','POST'])
@cross_origin()
def index():
    try:
        age=float(request.form['age'])
        yrs_married=float(request.form['yrs_married'])
        children=float(request.form['children'])
        rel=float(request.form['religious'])
        rmarr=float(request.form['rating_of_marriage'])
        educ=float(request.form['education'])
        occ=float(request.form['occupation'])
        hocc=float(request.form['h_occupation'])
        a1=np.array([0.0,0.0,0.0,0.0,0.0])
        a2=np.array([0.0,0.0,0.0,0.0,0.0])
        if(occ==1):
            pass
        else:
            a1[int(occ)-2]=1.0
        if(hocc==1):
            pass
        else:
            a2[int(hocc)-2]=1.0
        a3=np.append(a1,a2)
        final_arr=np.append(a3,[rmarr,age,yrs_married,children,rel,educ])
        model=load(open("model.pkl",'rb'))
        prediction=model.predict([final_arr])
        if(prediction[0]==0):
            prediction="an extra marital affair is unlikely to happen"
        else:
            prediction="an extra marital affair is Highly likely to happen"
        return render_template('results.html',prediction=prediction)
    except Exception as e:
        print('The Exception message is: ',e)
        return 'Something Went Wrong. Go back and try again.'


if __name__=="__main__":
    app.run(debug=True)

