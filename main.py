# importement
from flask import Flask, request, render_template
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import model


# application
app = Flask(__name__, template_folder="templates")



@app.route("/submit", methods=["POST"]) 
def submit() : 
    ## print("something happened")
    if request.method == 'POST' : 
        text = request.form["text"]
        #print(text)
        result = model.predict(text)
        #print(result)
    
    color = None
    if result.lower() == 'fake' : 
        color = "red"

    else : 
        color = "green"

    return render_template("predict.html", prediction=result, color = color)

@app.route("/")
def display() : 
    return render_template("index.html")

