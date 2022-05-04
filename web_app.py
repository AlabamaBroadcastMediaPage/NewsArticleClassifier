import numpy as np
import pandas as pd
import streamlit as st
import requests

st.write("""
# News Article Classifier App

### Classify your news articles with different machine learning models!
""")

article_content = st.text_input('Article to classify', 'Enter text here')
model = st.radio(
    "What machine learning model do you want to use?",
    ('Linear Regression', 'Logistic Regression', 'Random Forest Classification'))

if st.button('Classify'):

    if(model=='Linear Regression'):
        model_num = 0
    elif(model =='Logistic Regression'):
        model_num=1
    else:
        model_num=2

    url = "https://127.0.0.1:8888/getclassification"
    my_headers = {
    'Authorization': 'XXXXX',}
    data = { 
    "q": {
        "content": article_content,
        "model": model_num 
    }}
    r = requests.get(url, headers=my_headers, json=data)
    st.write(r.content)

