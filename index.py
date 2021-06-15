# GitHub
from flask import Flask
import json

dataJS = ""

with open("data.json", "r") as file:
    dataJS = json.load(file)

app = Flask(__name__)

@app.route('/')
def index():
    return "Veremos que pasa, aguante Aka!!!! <a href='dataMayor/RESUMEN_ContextoActualEcommerce.xlsx' >Repo</a> <a href='RESUMEN_ContextoActualEcommerce.rar' >RepoRar</a>"

@app.route('/data')
def data():
    return dataJS