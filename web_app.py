import numpy as np
import pandas as pd
import streamlit as st
import requests
from flask import Flask
import api_web



st.write("""
# News Article Classifier App

### Classify your news articles with different machine learning models!
""")

st.write("Who is the author of the article?")
author = st.text_input('Author name')
st.write("How many positive sentences does this article have?")
positive_num = st.number_input('Positive sentences', step=1, min_value=0)
st.write("How many negative sentences does this article have?")
negative_num = st.number_input('Negative sentences', step=1, min_value=0)


model = st.radio(
    "What machine learning model do you want to use?",
    ('Logistic Regression', 'Random Forest Classification'))

if st.button('Classify'):

    if(model =='Logistic Regression'):
        model_num=1
    else:
        model_num=2

    url = "https://localhost:8888/getclassification"
    my_headers = {
    'Authorization': 'XXXXX',}
    data = { 
    "q": {
        "author": author,
        "pos": positive_num,
        "neg": negative_num,
        "model": model_num 
    }}
    r = requests.get(url, headers=my_headers, json=data)
    st.write(r.content)

api_web.startlocal()