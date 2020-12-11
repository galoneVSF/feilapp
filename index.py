# GitHub
from flask import Flask
import json

dataJS = ""

with open("data.json", "r") as file:
    dataJS = json.load(file)

app = Flask(__name__)

@app.route('/')
def index():
    return "Veremos que pasa, aguante Aka!!!!"

@app.route('/data')
def data():
    return dataJS