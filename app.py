# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:47:18 2020

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 10:28:56 2020

@author: user
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def inddex():
    return render_template('home.html')
@app.route('/symptomspredict',methods=["POST","GET"])
def symptomspredict():
    return render_template('symptomspredict.html')
@app.route('/predict2')
def predict2():
    return render_template('predict2.html')
@app.route('/contactus')
def contactus():
    return render_template('contactus.html')
@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    
    name=request.form['name']
    """int_features = [float(x) for x in request.form.values()]
    #print(int_features)
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)"""
    
    
    int_features=[]
    
   # age=request.form['age']
    #gender=request.form['gender']
    onthyroxine=request.form['onthyroxine']
    query_hypo=request.form['query_hypo']
    tsh=request.form['tsh']
    t3=request.form['t3']
    tt4=request.form['tt4']
    fti=request.form['fti']
    
    int_features.append(onthyroxine)
    int_features.append(query_hypo)
    int_features.append(tsh)
    int_features.append(t3)
    int_features.append(tt4)
    int_features.append(fti)
    
    print(int_features)

    
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    print(type(output))
    #print(output)
    if(output==1):
        output="Normal"
    elif(output==2):
        output="Hyper Thyroidism"
    elif(output==3):
        output="Hypo Thyroidism"
    else:
        output="Please provide valid data..!"
    print(type(output))
    return render_template('predict2.html', prediction_text=output)
    #return render_template('index.html', prediction_text=name+' condition is '+output)

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)