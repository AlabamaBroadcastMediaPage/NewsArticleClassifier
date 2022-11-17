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
# Tájszólás-fordító alkalmazás

### Fordítsd a szöveged különböző tájszólásokra nyelvfeldolgozó algoritmusok segítségével!
""")

st.write("Szöveg")
text = st.text_input('Ide Írd a szöveget!')
accent = st.selectbox('Milyen tájszólásra szeretnéd fordítani?',('Szegedi', 'Eszperente'))


if st.button('Fordítás'):
    #url = "http://peterpottr.pythonanywhere.com/getclassification"
    url = "http://127.0.0.1:5000/translate_accent"
    my_headers = {
    'Authorization': 'XXXXX',}
    data = { 
    "q": {
        "text": text,
        "accent": accent
    }}

    r = requests.get(url, headers=my_headers, json=data)
    st.write(r.text)
