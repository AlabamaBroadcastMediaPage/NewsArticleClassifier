from urllib import response
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/getclassification", methods=['GET'])
def hello():
    return request.json['q']

if __name__ == "__main__":
    app.run()