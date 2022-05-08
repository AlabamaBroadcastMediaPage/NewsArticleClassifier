from urllib import response
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/getclassification", methods=['GET'])
def serve_foo():
    
    
    accuracy = 0
    positive = True
    if(positive):
        outputString = "This article is mainly positive. I'm " + str(accuracy*100) + "% sure."
    else:
        outputString = "This article is mainly positive. I'm " + str(accuracy*100) + "% sure."
    return outputString

if __name__ == "__main__":
    app.run()