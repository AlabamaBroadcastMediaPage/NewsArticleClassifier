import pyrebase

config = {
    "apiKey": "AIzaSyAJA4A4XQIm0pHryfwMLEcZi2tZhDF-teY",
    "authDomain": "news-classifier-3a9db.firebaseapp.com",
    "databaseURL": "https://news-classifier-3a9db.firebaseio.com",
    "projectId": "news-classifier-3a9db",
    "storageBucket": "news-classifier-3a9db.appspot.com",
    "messagingSenderId": "654597504034",
    "appId": "1:654597504034:web:d8ac2747e65f653f7ade7b",
    "measurementId": "G-FRF6SPTYBN"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

filename = "models/model_1.pkl"
cloud_filename = "models/model_1.pkl"

storage.child(cloud_filename).put(filename)