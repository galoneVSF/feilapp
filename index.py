# GitHub
from flask import Flask, make_response, request
import json

dataJS = ""

with open("data.json", "r") as file:
    dataJS = json.load(file)

def transform(text_file_contents):
    return text_file_contents.replace("=", ",")

#app = Flask(__name__)
app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
    return app.send_static_file('introNew.html')

@app.route('/html')
def index():
    return """
        <html>
            <body>
                <h1>Transform a file demo</h1>

                <form action="/transform" method="post" enctype="multipart/form-data">
                    <input type="file" name="data_file" />
                    <input type="submit" />
                </form>
            </body>
        </html>
    """

#    return "Veremos que pasa, aguante Aka!!!! <a href='dataMayor/RESUMEN_ContextoActualEcommerce.xlsx' >Repo</a> <a href='RESUMEN_ContextoActualEcommerce.rar' >RepoRar</a>"


@app.route('/data')
def data():
    return dataJS
    
    
@app.route('/transform', methods=["POST"])
def transform_view():
    request_file = request.files['data_file']
    if not request_file:
        return "No file"

    file_contents = request_file.stream.read().decode("utf-8")

    result = transform(file_contents)

    response = make_response(result)
    response.headers["Content-Disposition"] = "attachment; filename=result.csv"
    return response