import pandas as pd
import numpy as np
import pickle
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS, cross_origin
import requests

# Load the linear regression wine model

def load_model(filename):
    pkl_file=open(filename, 'rb')
    lr_model=pickle.load(pkl_file)
    pkl_file.close()
    return lr_model

lr_model_wine=load_model('C:\\Users\\fhrt8\\Desktop\\DATA\\Jordan River\\models\\wine_model.pkl')

# Create a flask app

app=Flask(__name__)

#Establish default route

# @app.route('/')
# def default():
#     return redirect('/red_input')

@app.route('/', methods=["GET"])
def red_input():
    return render_template('Red_wine_input.html')

@app.route('/red_predict',methods=["GET","POST"])

def red_predict():
    if request.method=='GET':
        va=request.args.get('va')
        sul=request.args.get('sul')
        alc=request.args.get('alc')

        data_red_wine=pd.DataFrame([[va,sul,alc]])
        arr_red_predict=lr_model_wine.predict(data_red_wine)[0]
        arr_red_predict=int(round(arr_red_predict,0))
        return render_template('red_wine_quality_predict.html', va=va, sul=sul, alc=alc, arr_red_predict=arr_red_predict)
    ### --> HTML response
        
    #return "Unsupported request method,{}".format(request.method),400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)