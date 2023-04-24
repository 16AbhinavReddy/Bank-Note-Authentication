from fastapi import FastAPI
from Bank_Note import Bank_Note
import pickle 
import numpy as np
import pandas as pd

app = FastAPI()
pickle_in = open("classifier.pkl", 'rb')
model = pickle.load(pickle_in)

@app.get('/')

def home():
    return {'message' : 'hello world'}

@app.get('/{name}')

def get_name(name : str) :
    return {'Welcome to the server' : f'{name}'}

@app.post('/predict')

def predict_note(data : Bank_Note):
    data = data.dict()
    variance = data['variance']
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy = data['entropy']

    predict = model.predict([[variance, skewness, curtosis, entropy]])

    if (predict[0] > 0.5) :
        output = "Fake Note"
    else :
        output = "Actual Bank Note"
    
    return {'Prediction' : output}