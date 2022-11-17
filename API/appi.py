from urllib import response
from flask import Flask
from flask import request
from sklearn.linear_model import LogisticRegression
import pickle

app = Flask(__name__)
#not work
@app.route("/getdialect", methods=['GET'])
def serve_foo():
    
    pos = request.json['q']['pos']
    neg = request.json['q']['neg']
    dialect = request.json['q']['dialect']


    loaded_model = pickle.load(open("model2.pkl", 'rb'))

    loaded_model.show()
if __name__ == "__main__":
    app.run()