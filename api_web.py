from numpy import True_
import streamlit as st
import pyrebase

if not hasattr(st, 'already_started_server'):
    # Hack the fact that Python modules (like st) only load once to
    # keep track of whether this file already ran.
    st.already_started_server = True

    st.write('''
        The first time this script executes it will run forever because it's
        running a Flask server.

        Just close this browser tab and open a new one to see your Streamlit
        app.
    ''')

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
