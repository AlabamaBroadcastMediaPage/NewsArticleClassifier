from numpy import True_
import streamlit as st
import pyrebase

def startlocal():
    if not hasattr(st, 'already_started_server'):
        # Hack the fact that Python modules (like st) only load once to
        # keep track of whether this file already ran.
        from flask import Flask

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

        app.run(port=8888)
