# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 22:59:26 2020

@author: barbora.filova
"""


from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def homepage():
    return render_template("index.html")

@app.route('/nutrition')

def nutrition():
    return render_template("nutrition.html")

@app.route('/training')

def training():
    return render_template("training.html")

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=True)