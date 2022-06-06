from urllib import response
from flask import Flask
from flask import request
from sklearn.linear_model import LogisticRegression
import numpy as np
import pickle

app = Flask(__name__)

@app.route("/getclassification", methods=['GET'])
def serve_foo():
    
    pos = request.json['q']['pos']
    neg = request.json['q']['neg']
    author = request.json['q']['author']
    site = request.json['q']['site']


    loaded_model = pickle.load(open("models/model.pkl", 'rb'))

    data = [float(pos),float(neg),float(pos+neg)]
    predict = loaded_model.predict(data)

    if(predict>=0.5):
        outputString = "This article is mainly positive."
    else:
        outputString = "This article is mainly negative."
    return outputString

if __name__ == "__main__":
    app.run()