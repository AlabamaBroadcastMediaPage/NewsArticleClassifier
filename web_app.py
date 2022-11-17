import numpy as np
import pandas as pd
import streamlit as st
import requests
from flask import Flask
from io import StringIO
import nltk

nltk.download('punkt')

def articleSentenceClassification(content):
    pos_words = ['jó','gyönyörű','szép','pozitív','csodálatos','helyes','elfogadható','jobb','szebb']
    x=0
    y=0
    s_list = nltk.tokenize.sent_tokenize(content)
    for i in range(len(s_list)):
        for word in pos_words:
            if (s_list[i].find(word) != -1):
                x+=1
    y = len(s_list)-x
    st.write(x,y)
    return x,y

st.write("""
# News Article Classifier App

### Classify your news articles with different machine learning models!
""")

st.write("Who is the author of the article?")
author = st.text_input('Author name')
site = st.selectbox('What site hosted this article?',('Mandiner', 'Krónika Online', 'HVG'))

uploaded_file = st.file_uploader("Choose a file where you upload the article")
if uploaded_file is not None:
    article_content = StringIO(uploaded_file.getvalue().decode("utf-8")).read()
    pos_count,neg_count = articleSentenceClassification(article_content)

if st.button('Classify'):
    #url = "http://peterpottr.pythonanywhere.com/getclassification"
    url = "http://127.0.0.1:5000/translate_accent"
    my_headers = {
    'Authorization': 'XXXXX',}
    data = { 
    "q": {
        "author": author,
        "site": site,
        "pos": pos_count,
        "neg": neg_count
    }}
    r = requests.get(url, headers=my_headers, json=data)
    st.write(r.text)

