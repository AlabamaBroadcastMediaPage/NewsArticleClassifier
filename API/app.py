from urllib import response
from flask import Flask
from flask import request
from sklearn.linear_model import LogisticRegression
import pickle

app = Flask(__name__)

@app.route("/getclassification", methods=['GET'])
def serve_foo():
    
    pos = request.json['q']['pos']
    neg = request.json['q']['neg']
    author = request.json['q']['author']
    site = request.json['q']['site']


    loaded_model = pickle.load(open("model.pkl", 'rb'))

    

    accuracy = 0
    positive = True
    if(positive):
        outputString = "This article is mainly positive. I'm " + str(accuracy*100) + "% sure."
    else:
        outputString = "This article is mainly positive. I'm " + str(accuracy*100) + "% sure."
    return outputString

if __name__ == "__main__":
    app.run()